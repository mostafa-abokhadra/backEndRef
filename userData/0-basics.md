### peronally identifiable information (PII)

-  cover information that could directly or indirectly reveal an individual’s identity.
- including online identifiers like cookies and IP addresses

### National Institute of Standard and Technology

**defined pII** as:

PII is any information about an individual maintained by an agency, including (1) any information that can be used to distinguish or trace an individual‘s identity, such as name, social security number, date and place of birth, mother‘s maiden name, or biometric records; and (2) any other information that is linked or linkable to an individual, such as medical, educational, financial, and employment information.

### Importance

But why is all that so important? As a website admin, app creator or product owner, you need to be aware that visitors and users could share sensitive information with you. These traces might enable you to identify individuals, so you must handle such data carefully. From a legal standpoint, it could be a matter of breaches and violations with serious consequences. Grasping the bigger picture is crucial for your organization’s security and legal compliance.

### Types of PII

### **LInked Information also called direct identifiers**

Direct identifiers are unique to a person and can be used to identify an individual. A single direct identifier is typically enough to determine someone’s identity.

**examples**

![photo](https://piwik.pro/wp-content/uploads/2020/10/PII_vs_personal_data_Diagram_1-1536x1164.png)

### **Linkable information**:

concerns indirect identifiers or quasi-identifiers. They may not be able to identify a person on their own, but identification becomes possible when combined with another piece of information. For example, research shows that 87% of US citizens could be identified based on just their gender, ZIP code and date of birth. De-anonymization and re-identification techniques typically work when multiple sets of quasi-identifiers are connected and can be used to distinguish one person from another.

**exmples**

![photo](https://piwik.pro/wp-content/uploads/2020/10/PII_vs_personal_data_Diagram_2-1536x826.png)

### **sensetive PII**:

**Examples**

1. Unique identification numbers, such as driver’s license numbers, social security numbers (SSN), passport numbers and other government-issued ID numbers.
2. Biometric data, such as fingerprints and retinal scans.
3. inancial information, including bank account numbers and credit card numbers.
4. Medical records.
5. Electronic and digital account information, such as email addresses and internet account numbers.
6. Employee personnel records.
7. Password information.
8. School identification numbers.

### **non sensetive PII:**
- is information that may or may not be unique to an individual person. This type of data can be transmitted without being encrypted, and disclosure of it will not cause harm to the individuals that the data concerns.
- Non-sensitive PII tends to be publicly available
- Some data privacy regulations don’t require the protection of non-sensitive PII, but companies should still employ safeguards to limit the risks to individuals. 

**examples**:

1. A person’s full name.
2. Mother’s maiden name.
3. Social media nickname.
4. Telephone number.
5. IP address.
6. Place of birth.
7. Date of birth.
8. Geographical details (ZIP code, city, state, country, etc.).
9. Employment information.
10. Email address or mailing address.
11. Race or ethnicity.
12. Religion.

### protected health information (PHI)

is a subset of PII that refers explicitly to information processed by HIPAA-covered entities. When health information is combined with a personal identifier, the data becomes PHI.

**Identifiers recognized by Health Insurance Portability and Accountability Act (HIPAA) include:**

![photo](https://piwik.pro/wp-content/uploads/2020/10/PII_vs_personal_data_Diagram_3-1536x1496.png)

[Us-Departement-Of-Human-Services](https://www.hhs.gov/hipaa/index.html)

[HIPAAP-rivacy-Policy](https://www.hhs.gov/sites/default/files/ocr/privacy/hipaa/administrative/combined/hipaa-simplification-201303.pdf)

The HIPAA Privacy Rule ensures that PHI is shared and used only with patient permission or to coordinate patient care and services between covered entities. Organizations covered by HIPAA, such as healthcare providers, hospitals, insurers and their business associates, must follow strict rules specifying the types of PHI they can collect from individuals, disclose with others, or use for marketing purposes.

### Non-PII

- data that cannot be used on its own to trace, or identify a person.

**Examples**
1. Aggregated statistics on the use of product/service.
2. Partially or fully masked IP addresses.

>[!IMPORTANT]
> However, the classification of PII and non-PII is vague. Moreover, <mark>NIST doesn’t reference cookie IDs and device IDs</mark>, so many AdTech companies, advertisers, and publishers consider them non-PII. As we’ll see, this is in contrast to the definition of personal data, which treats such digital tackers as information that could identify an individual.

### Personal Data

General Data Protection Regulaion [GDPR](https://gdpr-info.eu/) defined personal data as any information relating to an identified or identifiable natural person (‘data subject’); an identifiable natural person is one who can be identified, directly or indirectly, in particular by reference to an identifier such as a name, an identification number, location data, an <mark>online identifier</mark> or to one or more factors specific to the physical, physiological, genetic, mental, economic, cultural or social identity of that natural person;

This definition applies to a person’s name and surname, as well as details that could identify that person. That’s the case when, for instance, you’re able to identify a visitor returning to your website with the help of a cookie or login information.

> [!IMPORTANT]
> Under GDPR, you can view cookies as personal data because, according to: Recital 30:
> Natural persons may be associated with online identifiers provided by their devices, applications, tools and protocols, such as internet protocol addresses, cookie identifiers or other identifiers such as radio frequency identification tags. This may leave traces which, in particular when combined with unique identifiers and other information received by the servers, may be used to create profiles of the natural persons and identify them.

The definition of personal data covers various pieces of information, such as:

1. Transaction history
2. IP addresses
3. Browser history
4. Posts on social media

>[!NOTE]
> Personal data encompasses a broader range of contexts than PII. In general, all PII is considered personal data, but not all personal data is PII. For example, attributes such as religion, ethnicity, sexual orientation or medical history can be categorized as personal data but not PII.


### Ref
- [PII](https://piwik.pro/blog/what-is-pii-personal-data/)
- [PHI](https://piwik.pro/glossary/protected-health-information-phi/)