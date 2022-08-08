---
icon: "cloud"
title: "Validation rules"
description: "Validation rules for the VAT tax return"
---

[Norwegian](https://skatteetaten.github.io/mva-meldingen/kompensasjon/forretningsregler/)

### Change log

| Date       | Changes                                                             |
| :--------- | :------------------------------------------------------------------ |
| 2022.06.30 | Added page for validation rules for tax return for VAT compensation |

## Validation rules

The validation rules are under development an new validation rules will be added.
The following validation rules are definded for the tax return for VAT compensation:

- The sum of the calculated VAT from each VAT line shall be equal to the total VAT in the VAT return
- The calculated VAT must be in accordance with the stated VAT-basis multiplied by the current VAT-rate
- Additional information is lacking for input VAT amounts that have been claimed deductable with opposite +/- sign
- VAT returns must not be sent in before the related tax period has ended (general industry)
- Compensation of input VAT must be declared with a VAT-basis and VAT-rate
- VAT returns must not be sent in before the related tax period has ended (primary industry)
- VAT returns for earlier tax periods should have been submitted
- VAT returns for earlier tax periods should have been submitted and therefore repayments for this tax period will not be paid
- Input VAT must be declared without a VAT-basis or VAT-rate
- Output VAT must be declared with a VAT-basis and VAT-rate
- Specification lines that apply to the reversal of input VAT given in VAT §9-6 and §9-7 require a remark
- Account number must be registered for VAT returns that require a repayment
- Deductions for input VAT would not normally be declared for VAT returns relating to one-off registrations
- Remarks must be valid for the given VAT code (expected VAT direction)
- Remarks must be valid for the given VAT code (opposite VAT direction)
- Tax return for VAT compensation can only be submitted for a valid term category (bi-monthly)
- The first tax return for VAT compensation in a calendar year must have a total of more than 20 000 NOK in VAT
- The tax return for VAT compensationsubmitted
- A tax return for VAT compensation submitted before deadline must have auditor attestation
- The tax return for VAT compensation cannot be submitted after the deadline unless there is an approved return or taxation from the Tax Authority for the term.
- A tax return for VAT compensation submitted after deadline must have a lower credit amount than the last submitted return or taxation from the Tax Authority

The following technical rules are defined for the purpose of validating the format and code lists:

- The tax return for VAT compensation should be in a valid format
- The specification lines should only use valid VAT codes
- The specification lines should only use valid VAT-rates
- The specification lines should only use valid specifications
- The specification lines should only use valid remarks in the 'utvalgt merknad' field
- The tax return for VAT compensation should only use a valid remark in the 'utvalgt merknad' field

Two logistical rules are also defined for the purpose of preventing early submission to the new system or submission of earlier VAT returns:

- The submission and validation service is not available before 01.01.2023
- The submission and validation of VAT returns from before 2023 is not available

## Detailed description of the validation rules

Validation of the tax return for VAT compensation is implemented with a set of rules that are run automatically to check the validity of the return.
The rules are designed so that they are both documentation of the rules for the return and runnable by the system.

Example of rule:

```kotlin {.line-numbers}
[1]     MvaMeldingsinnhold_GrunnlagGangerGjeldendeSats_FeilBeregnetMerverdiavgiftForAvgiftslinje(
[2]        "Beregnet avgift i avgiftslinje er ulik produktet av grunnlag og sats" {
[3]            valideringsregel {
[4]                mvaSpesifikasjonslinje
[5]                    .hvor { linje -> linje.grunnlag ikkeEr tomt }
[6]                    .skal { linje -> linje.grunnlag * linje.sats væreRundetNedTil linje.merverdiavgift }
[7]            }
[8]            alvorlighetsgrad { AVVIKENDE_SKATTEMELDING }
[9]        }
[10]    )
```

Each line can be translated to the following:

**Line 1 - Identifier**: This is the reference for the rule. Each rule has a unique identifier.

**Line 2 - Error message**: This is the error message that will be returned in the validation API if The VAT return is not in accordance with the requirement in the rule.

**Line 3-7 - Validation Rule**: This is the rule that defines what a valid VAT return should be.
If this rule is not met, the validation will fail.

**Line 8 - Severity**: This is the severity if the validation fails.
The following severity levels are defined : AVVIKENDE_SKATTEMELDING (anomalous VAT return), UGYLDIG_SKATTEMELDING (invalid vat return)

**Detailed Specification of the rules will be addes a the development of the tax return for VAT compensation progresses**

