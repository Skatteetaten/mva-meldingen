Frontpage in English

#Implementation guide for system-to-system submission of VAT-report

##Background

The MEMO-project is developing a new tax return for VAT compensation (VAT return). The goal of the MEMO-prosject is to achieve better compliance, equal competitive conditions, simplification for reporting businesses, and a more effctive administration of the VAT system. 

Some simplification is a result of changes in the VAT return; fever sources of errors, easier returns, and making it easier to fulfill the duty to provide information.

A new VAT return will also provide new opportunities for guidance and dialog through validation before submission, and reminders for tasks. In addition it will be possible to offer an increased degree of search and insight to acheive effectiveness and safety through digital reconciliation of the VAT return. There is also a desire for better interaction between accounting/ERP systems and Altinn/Tax Authority systems, for example automatic receipt for submitted VAT returns. 

##Whats new

- Common information structure and rules for all types of VAT returns
- Flexibility; codebased rather than fixed fields
  - From electronic forms to digital interaction
- Simpler to provide the correct information; remarks for return per line and in total:
  - Removes the need for remarks
  - Structured remarks for common cases
  - Free form remarks
  - Attachements
- Refund; reporting businesses can submit a KID for reimbursement
- Removing errors prior to submission by validation
- Each return has a unique identifier
- New visual interface for the VAT returns  
  
  
##Oveview of the new service - components, API and message flow
This illustration describes the architecture of the new solution


![mva-meldingen_oversikt.png](mva-meldingen_oversikt.png)

- And end-user system creates a VAT return through auser interface.
- The end-user system can execute operations on VAT returns through an API between the system and ALtinn 3.
- API's for validation, signing and submitting VAT returns will be available
- Existing functionality in Altinn 2, such as inbox, roles and rights will also be available in the new service.
- Reporting business, accountants and advisors can access submitted information, sign VAT returns and submitt returns to the tax authority.
- The tax authority will offer a portal solution where taxable persons can access submitted information, make changes and submit VAT returns. 
- Login and authentication of the end user or system is carried out using ID-porten or Maskinporten. 
