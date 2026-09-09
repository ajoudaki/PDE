#ifndef MFP_QUADRATIC_CHECKPOINT_PATHS_H
#define MFP_QUADRATIC_CHECKPOINT_PATHS_H

#include <filesystem>
#include <iostream>

// Check existing aliases only, not concurrent filesystem mutations. The
// caller may update a distinct output, including resuming its checkpoint.
inline bool distinct_checkpoint_output(const std::filesystem::path &output,
                                       const std::filesystem::path &input) {
  try {
    if (std::filesystem::weakly_canonical(std::filesystem::absolute(output)) ==
            std::filesystem::weakly_canonical(std::filesystem::absolute(input)) ||
        (std::filesystem::exists(output) && std::filesystem::exists(input) &&
         std::filesystem::equivalent(output, input))) {
      std::cerr << "checkpoint output aliases an input: " << input << '\n';
      return false;
    }
  } catch (const std::filesystem::filesystem_error &error) {
    std::cerr << "cannot establish checkpoint path identity: " << error.what() << '\n';
    return false;
  }
  return true;
}

#endif
