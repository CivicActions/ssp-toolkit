# SCAP tailored controls from DISA STIG for RHEL6

## References

- <https://github.com/OpenSCAP/openscap>
- <https://github.com/ComplianceAsCode/content>

### HIGH impact tailored controls

#### Enable FIPS Mode in GRUB2

- Rule ID: _xccdf_org.ssgproject.content_rule_grub2_enable_fips_mode_
- Full FIPS mode is not available in the AWS us-east cloud as the hardware is not guaranteed to be certified. However, this site makes use of FIPS compliant openssl software and SSL certificates.

#### Install Virus Scanning Software

- Rule ID: _xccdf_org.ssgproject.content_rule_install_antivirus_
- This site employs ClamAV for anti-virus scanning and updates the database daily.

#### Ensure Software Patches Installed

- Rule ID: _xccdf_org.ssgproject.content_rule_security_patches_up_to_date_
- Software patches are installed twice monthly.

### MEDIUM impact tailored controls

#### Install Smart Card Packages For Multifactor Authentication

- Rule ID: _xccdf_org.ssgproject.content_rule_install_smartcard_packages_
- Console and smart card logins are disallowed.

#### Enable Smart Card Login

- Rule ID: _xccdf_org.ssgproject.content_rule_smartcard_auth_
- Console and smart card logins are disallowed.

#### Set Lockout Time for Failed Password Attempts

- Rule ID: _xccdf_org.ssgproject.content_rule_accounts_passwords_pam_faillock_unlock_time-storage_disabled_
- Passwords are only used after SSH key login by administrators to achieve root access. Only administrators have accounts; two-factor authentication is used and the accounts are audited monthly.

#### Set Password Maximum Consecutive Repeating Characters

- Rule ID: _xccdf_org.ssgproject.content_rule_accounts_password_pam_maxrepeat_
- Passwords are only used after SSH key login by administrators to achieve root access. Only administrators have accounts; two-factor authentication is used and the accounts are audited monthly.

