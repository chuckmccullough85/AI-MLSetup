#!/usr/bin/env python3
"""
AI Security Course - Setup Verification Script

This script verifies that your development environment is properly configured
for the AI Security course. It checks Python installation, package availability,
and basic functionality.

Usage:
    python verify_setup.py

Requirements:
    - Python 3.10+
    - Virtual environment (recommended)
    - Packages from requirements.txt
"""

import sys
import os
import subprocess
import importlib
from pathlib import Path


class SetupVerifier:
    """Comprehensive setup verification for AI Security course"""
    
    def __init__(self):
        self.errors = []
        self.warnings = []
        self.success_count = 0
        self.total_checks = 0
        
    def print_header(self):
        """Print verification header"""
        print("=" * 60)
        print("🔐 AI SECURITY COURSE - SETUP VERIFICATION")
        print("=" * 60)
        print()
        
    def print_section(self, title):
        """Print section header"""
        print(f"\n📋 {title}")
        print("-" * 40)
        
    def check_item(self, description, check_function):
        """Execute a check and track results"""
        self.total_checks += 1
        try:
            result = check_function()
            if result:
                print(f"✅ {description}")
                self.success_count += 1
                return True
            else:
                print(f"❌ {description}")
                self.errors.append(description)
                return False
        except Exception as e:
            print(f"❌ {description} - Error: {e}")
            self.errors.append(f"{description} - {e}")
            return False
            
    def warn_item(self, description):
        """Add a warning"""
        print(f"⚠️  {description}")
        self.warnings.append(description)
        
    def check_python_version(self):
        """Verify Python version is 3.10+"""
        version = sys.version_info
        if version.major >= 3 and version.minor >= 10:
            print(f"✅ Python version: {version.major}.{version.minor}.{version.micro}")
            return True
        else:
            print(f"❌ Python version: {version.major}.{version.minor}.{version.micro} (requires 3.10+)")
            return False
            
    def check_virtual_environment(self):
        """Check if running in virtual environment"""
        # Check common indicators of virtual environment
        venv_indicators = [
            'VIRTUAL_ENV' in os.environ,
            'CONDA_DEFAULT_ENV' in os.environ,
            hasattr(sys, 'real_prefix'),  # virtualenv
            (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix)  # venv
        ]
        
        if any(venv_indicators):
            venv_name = os.environ.get('VIRTUAL_ENV', os.environ.get('CONDA_DEFAULT_ENV', 'Unknown'))
            venv_name = Path(venv_name).name if venv_name != 'Unknown' else 'Unknown'
            print(f"✅ Virtual environment active: {venv_name}")
            return True
        else:
            self.warn_item("Not running in virtual environment (recommended but not required)")
            return True  # Don't fail the check, just warn
            
    def check_package_import(self, package_name):
        """Check if a package can be imported"""
        try:
            module = importlib.import_module(package_name)
            version = getattr(module, '__version__', 'Unknown')
            return f"{package_name} v{version}"
        except ImportError:
            return None
            
    def check_essential_packages(self):
        """Verify essential packages are installed"""
        essential_packages = [
            'numpy',
            'pandas',
            'matplotlib',
            'requests',
            'jupyter'
        ]
        
        missing_packages = []
        installed_packages = []
        
        for package in essential_packages:
            result = self.check_package_import(package)
            if result:
                installed_packages.append(result)
            else:
                missing_packages.append(package)
                
        # Print results
        for pkg in installed_packages:
            print(f"✅ {pkg}")
            
        for pkg in missing_packages:
            print(f"❌ {pkg} - Not installed")
            
        return len(missing_packages) == 0
        
    def check_data_manipulation(self):
        """Test basic data manipulation capabilities"""
        try:
            import numpy as np
            import pandas as pd
            
            # Create test data
            data = np.random.rand(5, 3)
            df = pd.DataFrame(data, columns=['A', 'B', 'C'])
            
            # Basic operations
            result = df.mean().sum()
            
            return isinstance(result, (int, float)) and not np.isnan(result)
        except Exception:
            return False
            
    def check_visualization(self):
        """Test matplotlib functionality"""
        try:
            import matplotlib.pyplot as plt
            import numpy as np
            
            # Create a simple plot (don't display)
            plt.ioff()  # Turn off interactive mode
            fig, ax = plt.subplots(figsize=(6, 4))
            x = np.linspace(0, 10, 100)
            y = np.sin(x)
            ax.plot(x, y)
            plt.close(fig)  # Close to free memory
            
            return True
        except Exception:
            return False
            
    def check_network_connectivity(self):
        """Test network connectivity for package downloads"""
        try:
            import requests
            response = requests.get('https://pypi.org', timeout=5)
            return response.status_code == 200
        except Exception:
            return False
            
    def check_file_permissions(self):
        """Check if we can create/write files in current directory"""
        try:
            test_file = Path('test_permissions.tmp')
            test_file.write_text('test')
            test_file.unlink()  # Delete test file
            return True
        except Exception:
            return False
            
    def run_security_simulation(self):
        """Run a simple AI security simulation"""
        try:
            import numpy as np
            import pandas as pd
            
            # Simulate security threat detection
            np.random.seed(42)
            
            # Generate synthetic security data
            n_samples = 100
            normal_traffic = np.random.normal(0.3, 0.1, n_samples // 2)
            anomalous_traffic = np.random.normal(0.8, 0.2, n_samples // 2)
            
            # Combine data
            traffic_data = np.concatenate([normal_traffic, anomalous_traffic])
            labels = [0] * (n_samples // 2) + [1] * (n_samples // 2)
            
            # Create DataFrame
            df = pd.DataFrame({
                'traffic_intensity': traffic_data,
                'is_threat': labels
            })
            
            # Simple threshold-based detection
            threshold = 0.6
            predictions = (df['traffic_intensity'] > threshold).astype(int)
            
            # Calculate accuracy
            accuracy = (predictions == df['is_threat']).mean()
            
            print(f"   Security simulation accuracy: {accuracy:.2%}")
            return accuracy > 0.7  # Expect at least 70% accuracy
            
        except Exception as e:
            print(f"   Simulation error: {e}")
            return False
    
    def print_summary(self):
        """Print verification summary"""
        print("\n" + "=" * 60)
        print("📊 VERIFICATION SUMMARY")
        print("=" * 60)
        
        success_rate = (self.success_count / self.total_checks) * 100
        print(f"✅ Successful checks: {self.success_count}/{self.total_checks} ({success_rate:.1f}%)")
        
        if self.warnings:
            print(f"⚠️  Warnings: {len(self.warnings)}")
            for warning in self.warnings:
                print(f"   • {warning}")
                
        if self.errors:
            print(f"❌ Errors: {len(self.errors)}")
            for error in self.errors:
                print(f"   • {error}")
        else:
            print("🎉 No errors found!")
            
        print("\n" + "=" * 60)
        
        if success_rate >= 90:
            print("🚀 EXCELLENT! Your setup is ready for the AI Security course!")
        elif success_rate >= 75:
            print("👍 GOOD! Minor issues detected, but you should be able to proceed.")
        else:
            print("⚠️  ATTENTION! Several issues detected. Please review and fix errors.")
            
        print("=" * 60)
    
    def run_all_checks(self):
        """Run complete verification suite"""
        self.print_header()
        
        # Python Environment Checks
        self.print_section("Python Environment")
        self.check_python_version()
        self.check_virtual_environment()
        self.check_item("File write permissions", self.check_file_permissions)
        
        # Package Checks
        self.print_section("Package Installation")
        self.check_item("Essential packages installed", self.check_essential_packages)
        self.check_item("Data manipulation (NumPy/Pandas)", self.check_data_manipulation)
        self.check_item("Visualization (Matplotlib)", self.check_visualization)
        
        # Connectivity and Functionality
        self.print_section("Connectivity and Functionality")
        self.check_item("Network connectivity (PyPI)", self.check_network_connectivity)
        self.check_item("AI Security simulation", self.run_security_simulation)
        
        # Print final summary
        self.print_summary()
        
        return len(self.errors) == 0


def main():
    """Main verification function"""
    try:
        verifier = SetupVerifier()
        success = verifier.run_all_checks()
        
        # Additional helpful information
        print("\n💡 Additional Information:")
        print(f"   Python executable: {sys.executable}")
        print(f"   Current directory: {os.getcwd()}")
        print(f"   Platform: {sys.platform}")
        
        # Exit with appropriate code
        sys.exit(0 if success else 1)
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Verification interrupted by user.")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ Unexpected error during verification: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
