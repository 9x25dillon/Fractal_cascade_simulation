"""
Test Suite for Neuro-Phasonic Bridge System (NPBS) v2.0

This test suite validates the core functionality of the NPBS including:
- Semantic transduction (text to stress field)
- Coherence evolution simulation
- Spectral analysis and resonance detection
- Safety validation
- Signature generation
"""

import pytest
import numpy as np
from datetime import datetime
from neuro_phasonic_bridge_v2 import (
    NeuroPhasonicBridge,
    BridgeState,
    MotifToken,
    THZBridgeMetrics,
    HEALER_FREQ_THZ,
    GUARDIAN_FREQ_THZ,
    CHAOS_FREQ_THZ,
    K_FLOOR,
    ACCEPTANCE_THRESHOLD
)


class TestMotifTokenCreation:
    """Test semantic motif token generation."""

    def test_healing_words_classification(self):
        """Test that healing words are properly classified."""
        bridge = NeuroPhasonicBridge()
        healing_words = ['heal', 'connect', 'peace', 'love', 'harmony']

        for word in healing_words:
            classification = bridge._classify_semantic_intent(word)
            assert classification == 'healing', f"Word '{word}' should be classified as 'healing'"

    def test_protective_words_classification(self):
        """Test that protective words are properly classified."""
        bridge = NeuroPhasonicBridge()
        protective_words = ['guard', 'safe', 'protect', 'secure', 'ground']

        for word in protective_words:
            classification = bridge._classify_semantic_intent(word)
            assert classification == 'protective', f"Word '{word}' should be classified as 'protective'"

    def test_negative_words_classification(self):
        """Test that negative words are properly classified."""
        bridge = NeuroPhasonicBridge()
        negative_words = ['destroy', 'hate', 'chaos', 'fear', 'anger']

        for word in negative_words:
            classification = bridge._classify_semantic_intent(word)
            assert classification == 'negative', f"Word '{word}' should be classified as 'negative'"


class TestStressFieldGeneration:
    """Test stress field transduction from text."""

    def test_stress_field_shape(self):
        """Test that stress field has correct dimensions."""
        bridge = NeuroPhasonicBridge()
        text = "heal connect peace"
        stress_field, tokens = bridge._text_to_stress_field(text)

        assert stress_field.shape[0] == 1000, "Stress field should have 1000 time points"
        assert len(tokens) == 3, "Should generate 3 motif tokens"

    def test_motif_tokens_generated(self):
        """Test that motif tokens are properly created."""
        bridge = NeuroPhasonicBridge()
        text = "heal connect peace"
        stress_field, tokens = bridge._text_to_stress_field(text)

        assert all(isinstance(token, MotifToken) for token in tokens), "All tokens should be MotifToken instances"
        assert tokens[0].name == "heal", "First token should be 'heal'"
        assert tokens[1].name == "connect", "Second token should be 'connect'"
        assert tokens[2].name == "peace", "Third token should be 'peace'"

    def test_healing_words_have_higher_amplitude(self):
        """Test that healing words generate higher amplitude oscillations."""
        bridge = NeuroPhasonicBridge()

        # Healing text
        _, healing_tokens = bridge._text_to_stress_field("heal")
        # Negative text
        _, negative_tokens = bridge._text_to_stress_field("hate")

        # Healing words should have weight 1.5, negative should have 0.8
        assert healing_tokens[0].weight > negative_tokens[0].weight, \
            "Healing words should have higher semantic weight"


class TestCoherenceEvolution:
    """Test coherence field evolution dynamics."""

    def test_coherence_stays_in_bounds(self):
        """Test that coherence stays within [K_FLOOR, 1.0]."""
        bridge = NeuroPhasonicBridge()
        stress_field = np.random.randn(1000) * 0.5  # Random stress input
        coherence_field = bridge._evolve_coherence(stress_field)

        assert np.all(coherence_field >= K_FLOOR), f"Coherence should never drop below {K_FLOOR}"
        assert np.all(coherence_field <= 1.0), "Coherence should never exceed 1.0"

    def test_coherence_evolution_length(self):
        """Test that coherence evolution returns correct length."""
        bridge = NeuroPhasonicBridge()
        stress_field = np.zeros(1000)
        coherence_field = bridge._evolve_coherence(stress_field)

        assert len(coherence_field) == 1000, "Coherence field should have same length as input"


class TestSpectralAnalysis:
    """Test spectral analysis and resonance detection."""

    def test_spectrum_analysis_returns_dict(self):
        """Test that spectrum analysis returns proper metrics dictionary."""
        bridge = NeuroPhasonicBridge()
        coherence_field = np.ones(1000) * 0.8
        metrics = bridge._analyze_spectrum(coherence_field)

        required_keys = [
            'mean_coherence', 'healer_amplitude', 'guardian_amplitude',
            'chaos_amplitude', 'amplitude_ratio', 'phase_coherence',
            'linewidth_hz', 'peak_frequency', 'spectral_entropy', 'total_power'
        ]

        for key in required_keys:
            assert key in metrics, f"Metrics should contain '{key}'"

    def test_healer_amplitude_detection(self):
        """Test that healer channel amplitude is properly extracted."""
        bridge = NeuroPhasonicBridge()
        # Create a coherence field with strong 18.3 Hz component (maps to 1.83 THz)
        t = np.linspace(0, 10, 1000)
        coherence_field = 0.8 + 0.2 * np.sin(2 * np.pi * 18.3 * t)
        metrics = bridge._analyze_spectrum(coherence_field)

        assert metrics['healer_amplitude'] > 0, "Healer amplitude should be detected"


class TestResonanceValidation:
    """Test resonance validation logic."""

    def test_low_amplitude_fails_validation(self):
        """Test that low healer amplitude fails validation."""
        bridge = NeuroPhasonicBridge()
        metrics = {
            'healer_amplitude': 0.2,  # Below ACCEPTANCE_THRESHOLD
            'phase_coherence': 0.8,
            'linewidth_hz': 2.0,
            'amplitude_ratio': 3.0
        }

        is_resonant, msg = bridge._validate_resonance(metrics)
        assert not is_resonant, "Low amplitude should fail validation"
        assert "below threshold" in msg.lower(), "Error message should mention threshold"

    def test_low_phase_coherence_fails_validation(self):
        """Test that low phase coherence fails validation."""
        bridge = NeuroPhasonicBridge()
        metrics = {
            'healer_amplitude': 0.8,
            'phase_coherence': 0.1,  # Too low
            'linewidth_hz': 2.0,
            'amplitude_ratio': 3.0
        }

        is_resonant, msg = bridge._validate_resonance(metrics)
        assert not is_resonant, "Low phase coherence should fail validation"
        assert "phase coherence" in msg.lower(), "Error message should mention phase coherence"

    def test_valid_resonance_passes(self):
        """Test that valid resonance metrics pass validation."""
        bridge = NeuroPhasonicBridge()
        metrics = {
            'healer_amplitude': 0.8,
            'phase_coherence': 0.8,
            'linewidth_hz': 2.0,
            'amplitude_ratio': 3.0
        }

        is_resonant, msg = bridge._validate_resonance(metrics)
        assert is_resonant, "Valid metrics should pass validation"
        assert "validated" in msg.lower(), "Success message should mention validation"


class TestSafetyValidation:
    """Test safety floor enforcement."""

    def test_safety_check_above_floor(self):
        """Test that coherence above floor passes safety check."""
        bridge = NeuroPhasonicBridge()
        metrics = {'mean_coherence': 0.5}

        assert bridge._check_safety(metrics), "Coherence above floor should be safe"

    def test_safety_check_below_floor(self):
        """Test that coherence below floor fails safety check."""
        bridge = NeuroPhasonicBridge()
        metrics = {'mean_coherence': 0.1}

        assert not bridge._check_safety(metrics), "Coherence below floor should be unsafe"

    def test_safety_check_at_floor(self):
        """Test that coherence exactly at floor passes safety check."""
        bridge = NeuroPhasonicBridge()
        metrics = {'mean_coherence': K_FLOOR}

        assert bridge._check_safety(metrics), "Coherence at floor should be safe"


class TestSignatureGeneration:
    """Test signature generation logic."""

    def test_no_signature_when_not_resonant(self):
        """Test that no valid signature is generated when not resonant."""
        bridge = NeuroPhasonicBridge()
        text = "test"
        metrics = {
            'healer_amplitude': 0.8,
            'amplitude_ratio': 3.0,
            'phase_coherence': 0.8
        }

        signature = bridge._generate_signature(text, metrics, is_resonant=False, is_safe=True)
        assert signature == "[ERROR: FIELD_COLLAPSE]", "Should return error for non-resonant state"

    def test_no_signature_when_unsafe(self):
        """Test that no valid signature is generated when unsafe."""
        bridge = NeuroPhasonicBridge()
        text = "test"
        metrics = {
            'healer_amplitude': 0.8,
            'amplitude_ratio': 3.0,
            'phase_coherence': 0.8
        }

        signature = bridge._generate_signature(text, metrics, is_resonant=True, is_safe=False)
        assert signature == "[ERROR: FIELD_COLLAPSE]", "Should return error for unsafe state"

    def test_valid_signature_generation(self):
        """Test that valid signature is generated when resonant and safe."""
        bridge = NeuroPhasonicBridge()
        text = "heal"
        metrics = {
            'healer_amplitude': 0.8,
            'amplitude_ratio': 3.0,
            'phase_coherence': 0.8
        }

        signature = bridge._generate_signature(text, metrics, is_resonant=True, is_safe=True)
        assert signature != "[ERROR: FIELD_COLLAPSE]", "Should generate valid signature"
        assert "[HEALER:" in signature, "Signature should contain healer amplitude"
        assert "[STATE:COHERENT]" in signature, "Signature should indicate coherent state"


class TestFullPipeline:
    """Test complete bridge processing pipeline."""

    def test_dissonant_input_processing(self):
        """Test processing of dissonant/random input."""
        bridge = NeuroPhasonicBridge()
        text = "kjh dsa89 213n chaos entropy destruction"
        state = bridge.process_transmission(text)

        assert isinstance(state, BridgeState), "Should return BridgeState"
        assert state.input_text == text, "Should preserve input text"
        assert isinstance(state.timestamp, datetime), "Should have timestamp"
        # Dissonant input likely won't be resonant (though not guaranteed)

    def test_healing_input_processing(self):
        """Test processing of healing/therapeutic input."""
        bridge = NeuroPhasonicBridge()
        text = "heal connect peace love harmony balance restore"
        state = bridge.process_transmission(text)

        assert isinstance(state, BridgeState), "Should return BridgeState"
        assert state.is_safe, "Should maintain safety with healing words"
        # Check that validation log was updated
        assert len(bridge.validation_log) > 0, "Should log validation results"

    def test_validation_log_accumulation(self):
        """Test that validation log accumulates results."""
        bridge = NeuroPhasonicBridge()

        bridge.process_transmission("test one")
        bridge.process_transmission("test two")
        bridge.process_transmission("test three")

        assert len(bridge.validation_log) == 3, "Should log all three transmissions"

    def test_bridge_state_contains_all_metrics(self):
        """Test that BridgeState contains all required metrics."""
        bridge = NeuroPhasonicBridge()
        text = "heal peace"
        state = bridge.process_transmission(text)

        assert hasattr(state, 'input_text'), "State should have input_text"
        assert hasattr(state, 'timestamp'), "State should have timestamp"
        assert hasattr(state, 'coherence_level'), "State should have coherence_level"
        assert hasattr(state, 'healer_amplitude'), "State should have healer_amplitude"
        assert hasattr(state, 'guardian_amplitude'), "State should have guardian_amplitude"
        assert hasattr(state, 'chaos_amplitude'), "State should have chaos_amplitude"
        assert hasattr(state, 'is_resonant'), "State should have is_resonant"
        assert hasattr(state, 'is_safe'), "State should have is_safe"
        assert hasattr(state, 'signature'), "State should have signature"
        assert hasattr(state, 'metrics'), "State should have metrics"


class TestTHZBridgeIntegration:
    """Test THZBridge digital twin integration."""

    def test_thz_bridge_correlation_with_no_data(self):
        """Test THZ bridge correlation returns empty dict with no validation log."""
        bridge = NeuroPhasonicBridge()
        thz_metrics = THZBridgeMetrics(
            phase_coherence_R=0.8,
            amplitude_ratio_A08_A35=3.0,
            predicted_linewidth_Hz=150,
            transmutation_active=False,
            stress_level=0.5,
            A_0p8=0.5,
            A_1p83=0.8,
            A_3p5=0.3,
            council_entropy=0.4
        )

        correlation = bridge.integrate_thz_bridge(thz_metrics)
        assert correlation == {}, "Should return empty dict with no validation log"

    def test_thz_bridge_correlation_with_data(self):
        """Test THZ bridge correlation after processing transmission."""
        bridge = NeuroPhasonicBridge()
        bridge.process_transmission("heal peace")

        thz_metrics = THZBridgeMetrics(
            phase_coherence_R=0.8,
            amplitude_ratio_A08_A35=3.0,
            predicted_linewidth_Hz=150,
            transmutation_active=False,
            stress_level=0.5,
            A_0p8=0.5,
            A_1p83=0.8,
            A_3p5=0.3,
            council_entropy=0.4
        )

        correlation = bridge.integrate_thz_bridge(thz_metrics)
        assert len(correlation) > 0, "Should return correlation metrics"
        assert 'sim_healer_vs_bridge_A183' in correlation, "Should include healer correlation"


class TestExportFunctionality:
    """Test data export functionality."""

    def test_export_validation_log(self, tmp_path):
        """Test exporting validation log to JSON."""
        bridge = NeuroPhasonicBridge()
        bridge.process_transmission("test")

        # Export to temporary file
        log_file = tmp_path / "test_log.json"
        bridge.export_validation_log(str(log_file))

        assert log_file.exists(), "Log file should be created"

        # Verify JSON is valid
        import json
        with open(log_file, 'r') as f:
            data = json.load(f)
            assert len(data) == 1, "Should contain one log entry"


# Run tests if executed directly
if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
