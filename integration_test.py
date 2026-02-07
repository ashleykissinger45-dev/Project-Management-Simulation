"""
Integration test that exercises the CLI with automated inputs.
"""
import subprocess
import sys


def test_cli_interaction():
    """Test the CLI with automated inputs."""
    print("=" * 80)
    print("INTEGRATION TEST: CLI INTERACTION")
    print("=" * 80)
    print()
    
    # Test scenario selection and basic menu navigation
    # Simulate: Select project 2 (mobile app) → View status → View tasks → Exit
    test_input = "2\n1\n2\n1\n9\n"
    
    print("Testing CLI with automated inputs...")
    print("Commands: Select Mobile App → View Status → View Tasks → Filter All → Exit")
    print()
    
    try:
        result = subprocess.run(
            [sys.executable, "simulation_cli.py"],
            input=test_input,
            capture_output=True,
            text=True,
            timeout=10
        )
        
        output = result.stdout
        
        # Check for expected outputs
        checks = [
            ("Project selection menu", "Select a project scenario" in output),
            ("Project name displayed", "Fitness Tracking Mobile App" in output),
            ("Main menu shown", "MAIN MENU" in output),
            ("Status view", "PROJECT STATUS" in output or "Progress:" in output),
            ("Task list", "TASK LIST" in output or "Filter by status" in output),
            ("Exit message", "Thank you" in output or "Goodbye" in output)
        ]
        
        print("Validation Results:")
        all_passed = True
        for check_name, passed in checks:
            status = "✓" if passed else "✗"
            print(f"  {status} {check_name}")
            if not passed:
                all_passed = False
        
        print()
        
        if all_passed:
            print("✅ Integration test PASSED - All checks successful")
            return True
        else:
            print("⚠️ Integration test completed with warnings")
            print("\nOutput preview:")
            print("-" * 80)
            print(output[:1000])  # Show first 1000 chars
            print("-" * 80)
            return False
            
    except subprocess.TimeoutExpired:
        print("❌ Integration test FAILED - Timeout (CLI may be waiting for input)")
        return False
    except Exception as e:
        print(f"❌ Integration test FAILED - Error: {e}")
        return False


def test_demo_execution():
    """Test that the demo runs successfully."""
    print("=" * 80)
    print("INTEGRATION TEST: DEMO EXECUTION")
    print("=" * 80)
    print()
    
    try:
        result = subprocess.run(
            [sys.executable, "demo.py"],
            capture_output=True,
            text=True,
            timeout=15
        )
        
        output = result.stdout
        
        # Check for expected demo outputs
        checks = [
            ("Demo header", "DEMO" in output),
            ("Project info", "E-Commerce Web Application" in output),
            ("Phase 1", "PHASE 1" in output),
            ("Task assignment", "Assigned" in output or "ASSIGNMENT" in output),
            ("Simulation", "SIMULATING" in output or "Day" in output),
            ("Status report", "PROJECT STATUS" in output or "Progress:" in output),
            ("Demo complete", "DEMO COMPLETE" in output or "demonstration showed" in output)
        ]
        
        print("Validation Results:")
        all_passed = True
        for check_name, passed in checks:
            status = "✓" if passed else "✗"
            print(f"  {status} {check_name}")
            if not passed:
                all_passed = False
        
        print()
        
        if all_passed and result.returncode == 0:
            print("✅ Demo execution test PASSED")
            return True
        else:
            print("⚠️ Demo execution test completed with warnings")
            if result.returncode != 0:
                print(f"   Return code: {result.returncode}")
            return False
            
    except subprocess.TimeoutExpired:
        print("❌ Demo execution test FAILED - Timeout")
        return False
    except Exception as e:
        print(f"❌ Demo execution test FAILED - Error: {e}")
        return False


def test_unit_tests():
    """Test that the unit test suite passes."""
    print("=" * 80)
    print("INTEGRATION TEST: UNIT TEST SUITE")
    print("=" * 80)
    print()
    
    try:
        result = subprocess.run(
            [sys.executable, "test_simulation.py"],
            capture_output=True,
            text=True,
            timeout=10
        )
        
        output = result.stdout
        
        print(output)
        
        if result.returncode == 0 and "0 failed" in output:
            print("✅ Unit test suite PASSED")
            return True
        else:
            print("❌ Unit test suite FAILED")
            if result.stderr:
                print("Errors:")
                print(result.stderr)
            return False
            
    except Exception as e:
        print(f"❌ Unit test suite FAILED - Error: {e}")
        return False


def run_integration_tests():
    """Run all integration tests."""
    print("\n")
    print("*" * 80)
    print("PROJECT MANAGEMENT SIMULATION - INTEGRATION TESTS".center(80))
    print("*" * 80)
    print("\n")
    
    results = []
    
    # Run tests
    results.append(("Unit Tests", test_unit_tests()))
    results.append(("Demo Execution", test_demo_execution()))
    results.append(("CLI Interaction", test_cli_interaction()))
    
    # Summary
    print("\n")
    print("=" * 80)
    print("INTEGRATION TEST SUMMARY")
    print("=" * 80)
    print()
    
    for test_name, passed in results:
        status = "✅ PASSED" if passed else "❌ FAILED"
        print(f"{test_name}: {status}")
    
    print()
    
    total = len(results)
    passed_count = sum(1 for _, passed in results if passed)
    
    print(f"Total: {passed_count}/{total} tests passed")
    print("=" * 80)
    print()
    
    return all(passed for _, passed in results)


if __name__ == "__main__":
    success = run_integration_tests()
    sys.exit(0 if success else 1)
