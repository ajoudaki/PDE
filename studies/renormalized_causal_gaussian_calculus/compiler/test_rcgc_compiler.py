import unittest

from .rcgc_compiler import ActivationSignature, compile_mlp


class CompilerRegressionTest(unittest.TestCase):
    def test_kernel_has_one_term_per_parameter_block(self) -> None:
        for depth in (1, 2, 3, 7):
            compiled = compile_mlp(depth, ActivationSignature.identity())
            self.assertEqual(len(compiled.raw_kernel_terms), depth + 1)
            self.assertEqual(len(compiled.feature_velocities), depth + 1)

    def test_identity_kills_every_curvature_word(self) -> None:
        for depth in (1, 2, 3, 7):
            compiled = compile_mlp(depth, ActivationSignature.identity())
            self.assertEqual(compiled.curvature_words, ())

    def test_generic_depth_one_is_local_only(self) -> None:
        compiled = compile_mlp(1, ActivationSignature.nonlinear())
        self.assertEqual(len(compiled.curvature_words), 1)
        self.assertEqual(compiled.curvature_words[0].edge_word, ())
        self.assertEqual(
            compiled.curvature_words[0].promotion_class, "local_diagonal"
        )

    def test_generic_depth_two_emits_one_colour(self) -> None:
        compiled = compile_mlp(2, ActivationSignature.nonlinear("arctan"))
        words = compiled.curvature_words
        self.assertEqual(words[1].edge_word, ("2-", "2+"))
        self.assertEqual(words[1].colour_count, 1)
        self.assertEqual(words[1].promotion_class, "one_colour_return")

    def test_generic_depth_three_emits_nested_two_colour_word(self) -> None:
        compiled = compile_mlp(3, ActivationSignature.nonlinear("arctan"))
        nested = compiled.curvature_words[2]
        self.assertEqual(
            nested.factors,
            (
                "D_1",
                "G_2^*",
                "D_2",
                "G_3^*",
                "E_3",
                "G_3",
                "D_2",
                "G_2",
                "D_1",
            ),
        )
        self.assertEqual(nested.edge_word, ("2-", "3-", "3+", "2+"))
        self.assertEqual(nested.colour_count, 2)
        self.assertEqual(nested.promotion_class, "multi_colour_return")

    def test_invalid_depth_rejected(self) -> None:
        with self.assertRaises(ValueError):
            compile_mlp(0, ActivationSignature.identity())


if __name__ == "__main__":
    unittest.main()
