<svg width="100%" viewBox="0 0 680 470" role="img"><title>Figure 13: activity clock and Legendre moments</title><desc>Residual decays while the clock saturates; a neuron's history on the clock is projected onto a few moments; the weight error is a product of two tails.</desc>
<defs><marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></marker></defs>
<text class="th" x="40" y="30">Physical time t ∈ [0, ∞)</text>
<line x1="40" y1="170" x2="300" y2="170" class="arr" marker-end="url(#arrow)"/>
<line x1="40" y1="170" x2="40" y2="50" stroke="var(--b)" stroke-width="0.5"/>
<path d="M40 60 C70 75, 90 120, 120 140 C160 160, 220 166, 296 168" fill="none" stroke="#D85A30" stroke-width="2"/>
<text class="ts" x="128" y="122">residual ρ(t)</text>
<path d="M40 168 C70 140, 100 92, 140 78 C190 66, 240 64, 296 63" fill="none" stroke="#534AB7" stroke-width="2"/>
<line x1="40" y1="63" x2="300" y2="63" stroke="#534AB7" stroke-width="0.5" stroke-dasharray="3 3"/>
<text class="ts" x="200" y="54">clock τ(t) = ∫ρ → τ∞ &lt; ∞</text>
<text class="ts" x="170" y="188" text-anchor="middle">t</text>
<line x1="320" y1="110" x2="372" y2="110" class="arr" marker-end="url(#arrow)"/>
<text class="ts" x="346" y="98" text-anchor="middle">fold</text>
<text class="th" x="390" y="30">Activity clock τ ∈ [0, τ∞]</text>
<line x1="390" y1="170" x2="640" y2="170" stroke="var(--b)" stroke-width="0.5"/>
<line x1="390" y1="170" x2="390" y2="50" stroke="var(--b)" stroke-width="0.5"/>
<line x1="640" y1="165" x2="640" y2="175" stroke="var(--t)" stroke-width="1"/>
<text class="ts" x="640" y="188" text-anchor="middle">τ∞</text>
<path d="M390 130 C420 70, 450 70, 480 100 C510 135, 540 140, 570 110 C595 85, 620 80, 640 90" fill="none" stroke="#5F5E5A" stroke-width="1.5"/>
<path d="M390 125 C430 82, 470 88, 510 112 C550 132, 600 100, 640 92" fill="none" stroke="#534AB7" stroke-width="2" stroke-dasharray="6 3"/>
<text class="ts" x="400" y="62">one neuron's history (gray)</text>
<text class="ts" x="400" y="210">q Legendre moments (purple, dashed) per neuron</text>
<text class="th" x="40" y="262">Why few moments suffice: the error is a product of two tails</text>
<g class="c-purple"><rect x="40" y="282" width="180" height="62" rx="8" stroke-width="0.5"/><text class="th" x="130" y="304" text-anchor="middle" dominant-baseline="central">backward history b</text><text class="ts" x="130" y="326" text-anchor="middle" dominant-baseline="central">tail (I−Π_q) b small</text></g>
<g class="c-teal"><rect x="250" y="282" width="180" height="62" rx="8" stroke-width="0.5"/><text class="th" x="340" y="304" text-anchor="middle" dominant-baseline="central">forward history h</text><text class="ts" x="340" y="326" text-anchor="middle" dominant-baseline="central">tail (I−Π_q) h small</text></g>
<g class="c-coral"><rect x="460" y="282" width="180" height="62" rx="8" stroke-width="0.5"/><text class="th" x="550" y="304" text-anchor="middle" dominant-baseline="central">weight error</text><text class="ts" x="550" y="326" text-anchor="middle" dominant-baseline="central">small × small</text></g>
<text class="t" x="340" y="384" text-anchor="middle">∫ b hᵀ dτ − ∫ (Π_q b)(Π_q h)ᵀ dτ = ∫ ((I−Π_q) b)((I−Π_q) h)ᵀ dτ</text>
<text class="ts" x="340" y="410" text-anchor="middle">cross terms vanish by orthogonality, so the error decays like q⁻² rather than q⁻¹</text>
<text class="ts" x="340" y="432" text-anchor="middle">every neuron is kept; only its time axis is compressed</text>
</svg>