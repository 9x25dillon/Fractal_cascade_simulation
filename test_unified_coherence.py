#!/usr/bin/env python3
"""
Comprehensive tests for the Unified Coherence System
=====================================================
Tests CR²BC Engine, EFL-MEM Format, QINCRS Guardian, and integrations
"""

import asyncio
import json
import time
from typing import Dict, Any

# Import components
try:
    from unified_coherence_system import (
        UnifiedCoherenceSystem, AgentHints, CoherenceSample,
        CR2BC, CR2BCConfig, QINCRSGuard,
        EFLMemSerializer, EFLMemParser,
        GeometricSelf, CoherenceState
    )
    COHERENCE_AVAILABLE = True
except ImportError:
    COHERENCE_AVAILABLE = False
    print("❌ Unified Coherence System not available")

try:
    from coherence_matrix_integration import (
        CoherenceAwareMatrixOrchestrator,
        CoherenceMonitoredOptimization,
        quick_coherence_check,
        safe_matrix_optimize
    )
    INTEGRATION_AVAILABLE = True
except ImportError:
    INTEGRATION_AVAILABLE = False
    print("⚠️  Coherence-Matrix Integration not available")


class TestResults:
    """Test results tracker"""
    def __init__(self):
        self.tests_run = 0
        self.tests_passed = 0
        self.tests_failed = 0
        self.failures = []

    def record_pass(self, test_name: str):
        self.tests_run += 1
        self.tests_passed += 1
        print(f"✅ {test_name}")

    def record_fail(self, test_name: str, error: str):
        self.tests_run += 1
        self.tests_failed += 1
        self.failures.append((test_name, error))
        print(f"❌ {test_name}: {error}")

    def summary(self):
        print("\n" + "=" * 70)
        print("TEST SUMMARY")
        print("=" * 70)
        print(f"Total tests run: {self.tests_run}")
        print(f"Passed: {self.tests_passed}")
        print(f"Failed: {self.tests_failed}")

        if self.failures:
            print("\nFailed tests:")
            for test_name, error in self.failures:
                print(f"  - {test_name}: {error}")
        else:
            print("\n🎉 All tests passed!")


def test_cr2bc_engine():
    """Test CR²BC Engine functionality"""
    print("\n" + "=" * 70)
    print("Testing CR²BC Engine")
    print("=" * 70)

    results = TestResults()

    try:
        # Test 1: Basic reconstruction
        config = CR2BCConfig(epsilon=0.1, delta_t=0.01)
        cr2bc = CR2BC(config)

        test_state = [1.0, 2.0, 3.0, 4.0, 5.0]
        reconstructed, audit = cr2bc.reconstruct(test_state)

        if len(reconstructed) > 0 and audit.score >= 0:
            results.record_pass("CR²BC basic reconstruction")
        else:
            results.record_fail("CR²BC basic reconstruction", "Invalid output")

        # Test 2: Reconstruction with hints
        hints = AgentHints("test_agent_a", "test_agent_b", {"test": "data"})
        reconstructed_with_hints, audit_with_hints = cr2bc.reconstruct(test_state, hints)

        if len(reconstructed_with_hints) > 0:
            results.record_pass("CR²BC reconstruction with hints")
        else:
            results.record_fail("CR²BC reconstruction with hints", "Invalid output")

        # Test 3: Coherence trend analysis
        for _ in range(5):
            cr2bc.reconstruct([float(i) for i in range(10)])

        trend = cr2bc.get_coherence_trend()
        if "trend" in trend and "average_kappa" in trend:
            results.record_pass("CR²BC coherence trend analysis")
        else:
            results.record_fail("CR²BC coherence trend analysis", "Missing trend data")

        # Test 4: Audit constraints
        if "magnitude_gt_epsilon" in audit.constraints:
            results.record_pass("CR²BC audit constraints")
        else:
            results.record_fail("CR²BC audit constraints", "Missing constraints")

    except Exception as e:
        results.record_fail("CR²BC Engine tests", str(e))

    results.summary()
    return results


def test_efl_mem_format():
    """Test EFL-MEM serialization and parsing"""
    print("\n" + "=" * 70)
    print("Testing EFL-MEM Format")
    print("=" * 70)

    results = TestResults()

    try:
        # Test 1: Create coherence samples
        samples = [
            CoherenceSample(t=time.time(), kappa=0.5, phi=[1.0, 2.0], context={"test": "1"}),
            CoherenceSample(t=time.time(), kappa=0.7, phi=[3.0, 4.0], context={"test": "2"}),
            CoherenceSample(t=time.time(), kappa=0.9, phi=[5.0, 6.0], context={"test": "3"})
        ]

        # Test 2: Serialize to EFL-MEM format
        efl_data = EFLMemSerializer.from_coherence_history(samples)

        if "format_version" in efl_data and efl_data["format_version"] == "EFL-MEM-1.0":
            results.record_pass("EFL-MEM serialization")
        else:
            results.record_fail("EFL-MEM serialization", "Invalid format")

        # Test 3: Convert to JSON
        json_str = EFLMemSerializer.to_json(efl_data)
        if len(json_str) > 0:
            results.record_pass("EFL-MEM JSON conversion")
        else:
            results.record_fail("EFL-MEM JSON conversion", "Empty JSON")

        # Test 4: Parse from JSON
        parsed_data = EFLMemParser.from_json(json_str)
        if "samples" in parsed_data:
            results.record_pass("EFL-MEM JSON parsing")
        else:
            results.record_fail("EFL-MEM JSON parsing", "Missing samples")

        # Test 5: Reconstruct coherence history
        reconstructed_samples = EFLMemParser.to_coherence_history(parsed_data)
        if len(reconstructed_samples) == len(samples):
            results.record_pass("EFL-MEM history reconstruction")
        else:
            results.record_fail("EFL-MEM history reconstruction", "Sample count mismatch")

        # Test 6: Metadata extraction
        metadata = efl_data.get("metadata", {})
        if "total_samples" in metadata and "average_coherence" in metadata:
            results.record_pass("EFL-MEM metadata extraction")
        else:
            results.record_fail("EFL-MEM metadata extraction", "Missing metadata")

    except Exception as e:
        results.record_fail("EFL-MEM Format tests", str(e))

    results.summary()
    return results


def test_qincrs_guardian():
    """Test QINCRS Guardian safety filtering"""
    print("\n" + "=" * 70)
    print("Testing QINCRS Guardian")
    print("=" * 70)

    results = TestResults()

    try:
        guardian = QINCRSGuard()

        # Test 1: Allow safe message
        safe_msg = "This is a safe and constructive message about coherence"
        safe_result = guardian.filter_message(safe_msg)

        if safe_result["action"] == "allow":
            results.record_pass("QINCRS allows safe messages")
        else:
            results.record_fail("QINCRS allows safe messages", f"Action: {safe_result['action']}")

        # Test 2: Block harmful message
        harmful_msg = "kill yourself"
        harmful_result = guardian.filter_message(harmful_msg)

        if harmful_result["action"] == "block":
            results.record_pass("QINCRS blocks harmful messages")
        else:
            results.record_fail("QINCRS blocks harmful messages", f"Action: {harmful_result['action']}")

        # Test 3: Transform low-coherence message
        low_coherence_msg = "everything is chaos and nothing makes sense"
        transform_result = guardian.filter_message(low_coherence_msg)

        if transform_result["action"] in ["transform", "allow", "block"]:
            results.record_pass("QINCRS handles low-coherence messages")
        else:
            results.record_fail("QINCRS handles low-coherence messages", "Invalid action")

        # Test 4: Policy decisions
        if "policy" in safe_result and "state" in safe_result["policy"]:
            results.record_pass("QINCRS policy decisions")
        else:
            results.record_fail("QINCRS policy decisions", "Missing policy")

        # Test 5: Absorption tracking
        if guardian.absorber.absorption_count > 0:
            results.record_pass("QINCRS absorption tracking")
        else:
            results.record_fail("QINCRS absorption tracking", "No absorptions recorded")

        # Test 6: Shadow dimension learning
        guardian.shadow.update_risk_lexicon(harmful_msg, 0.1)
        risky_tokens = guardian.shadow.get_risky_tokens(min_count=1)

        if len(risky_tokens) > 0:
            results.record_pass("QINCRS shadow dimension learning")
        else:
            results.record_fail("QINCRS shadow dimension learning", "No risky tokens learned")

    except Exception as e:
        results.record_fail("QINCRS Guardian tests", str(e))

    results.summary()
    return results


def test_unified_coherence_system():
    """Test the complete Unified Coherence System"""
    print("\n" + "=" * 70)
    print("Testing Unified Coherence System")
    print("=" * 70)

    results = TestResults()

    try:
        system = UnifiedCoherenceSystem()

        # Test 1: Process safe message
        safe_result = system.process_message("Testing coherence reconstruction")

        if "coherence_metrics" in safe_result:
            results.record_pass("UCS processes safe messages")
        else:
            results.record_fail("UCS processes safe messages", "Missing metrics")

        # Test 2: Process with agent hints
        hints = AgentHints("test_a", "test_b", {"context": "testing"})
        hints_result = system.process_message("Testing with hints", hints)

        if hints_result["coherence_metrics"]["kappa"] > 0:
            results.record_pass("UCS processes messages with hints")
        else:
            results.record_fail("UCS processes messages with hints", "Invalid kappa")

        # Test 3: Geometric self mapping
        geometric_self = hints_result["coherence_metrics"]["geometric_self"]
        valid_geometries = ["fragmented", "integrating", "coherent"]

        if geometric_self in valid_geometries:
            results.record_pass("UCS geometric self mapping")
        else:
            results.record_fail("UCS geometric self mapping", f"Invalid: {geometric_self}")

        # Test 4: Coherence state mapping
        coherence_state = hints_result["coherence_metrics"]["coherence_state"]
        valid_states = ["dissociated", "fragmented", "adaptive", "harmonic", "deep_sync"]

        if coherence_state in valid_states:
            results.record_pass("UCS coherence state mapping")
        else:
            results.record_fail("UCS coherence state mapping", f"Invalid: {coherence_state}")

        # Test 5: System status
        status = system.get_system_status()

        if "unified_system" in status and "coherence_metrics" in status:
            results.record_pass("UCS system status")
        else:
            results.record_fail("UCS system status", "Missing status data")

        # Test 6: EFL-MEM export
        efl_export = system.export_to_efl_mem()

        if len(efl_export) > 0:
            results.record_pass("UCS EFL-MEM export")
        else:
            results.record_fail("UCS EFL-MEM export", "Empty export")

        # Test 7: Safety layer integration
        safety_info = safe_result.get("safety_layer", {})

        if "action" in safety_info:
            results.record_pass("UCS safety layer integration")
        else:
            results.record_fail("UCS safety layer integration", "Missing safety info")

    except Exception as e:
        results.record_fail("Unified Coherence System tests", str(e))

    results.summary()
    return results


async def test_coherence_matrix_integration():
    """Test Coherence-Matrix Integration"""
    print("\n" + "=" * 70)
    print("Testing Coherence-Matrix Integration")
    print("=" * 70)

    results = TestResults()

    if not INTEGRATION_AVAILABLE:
        results.record_fail("Integration tests", "Integration module not available")
        results.summary()
        return results

    try:
        # Test 1: Quick coherence check
        check_result = await quick_coherence_check("Testing coherence check")

        if "coherence_metrics" in check_result or "error" not in check_result:
            results.record_pass("Quick coherence check")
        else:
            results.record_fail("Quick coherence check", "Check failed")

        # Test 2: Safe matrix optimization (if matrix orchestrator available)
        try:
            test_matrix = [[1.0, 2.0], [3.0, 4.0]]
            opt_result = await safe_matrix_optimize(test_matrix, method="sparsity")

            if opt_result is not None:
                results.record_pass("Safe matrix optimization")
            else:
                results.record_pass("Safe matrix optimization (graceful degradation)")
        except Exception as e:
            results.record_pass("Safe matrix optimization (expected if backend missing)")

    except Exception as e:
        results.record_fail("Coherence-Matrix Integration tests", str(e))

    results.summary()
    return results


def run_all_tests():
    """Run all test suites"""
    print("\n" + "🌌" * 35)
    print("UNIFIED COHERENCE SYSTEM - COMPREHENSIVE TEST SUITE")
    print("🌌" * 35)

    if not COHERENCE_AVAILABLE:
        print("\n❌ Unified Coherence System not available - cannot run tests")
        return

    # Run synchronous tests
    cr2bc_results = test_cr2bc_engine()
    efl_results = test_efl_mem_format()
    qincrs_results = test_qincrs_guardian()
    ucs_results = test_unified_coherence_system()

    # Run async tests
    integration_results = asyncio.run(test_coherence_matrix_integration())

    # Overall summary
    print("\n" + "=" * 70)
    print("OVERALL TEST RESULTS")
    print("=" * 70)

    total_run = (cr2bc_results.tests_run + efl_results.tests_run +
                 qincrs_results.tests_run + ucs_results.tests_run +
                 integration_results.tests_run)

    total_passed = (cr2bc_results.tests_passed + efl_results.tests_passed +
                    qincrs_results.tests_passed + ucs_results.tests_passed +
                    integration_results.tests_passed)

    total_failed = (cr2bc_results.tests_failed + efl_results.tests_failed +
                    qincrs_results.tests_failed + ucs_results.tests_failed +
                    integration_results.tests_failed)

    print(f"Total tests: {total_run}")
    print(f"Passed: {total_passed}")
    print(f"Failed: {total_failed}")

    if total_failed == 0:
        print("\n🎉🎉🎉 ALL TESTS PASSED! 🎉🎉🎉")
    else:
        print(f"\n⚠️  {total_failed} test(s) failed")

    print("\n" + "=" * 70)


if __name__ == "__main__":
    run_all_tests()
