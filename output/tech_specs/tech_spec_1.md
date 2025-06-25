# Resume Upload Feature Technical Specification

## **Description**
The Resume Upload feature allows recruiters to upload candidates' resumes into the recruitment system efficiently. The system should support multiple file formats, ensure data integrity, and extract relevant information for candidate profiling.

## **Acceptance Criteria**
1. Users should be able to upload resumes in `.pdf`, `.doc`, and `.docx` formats.
2. The system must validate file types before upload and display appropriate error messages for invalid formats.
3. Uploaded resumes should be parsed to extract critical information, including candidate name, contact information, education, and work experience.
4. Recruiters must receive a confirmation message upon successful upload, indicating the total number of resumes uploaded.
5. In case of upload failure, error messages should be displayed clearly, detailing the reasons for failure.
6. The system should maintain a secure log of all upload attempts along with timestamps and user information.

## **Implementation Notes**
- **Frontend**: Utilize a React-based UI for dynamic feedback and validation during the file selection process. Implement drag-and-drop functionality for ease of use.
- **Backend**: Set up an API endpoint using Node.js with Express to handle resume uploads. The endpoint should accept multipart/form-data for handling file uploads.
- **File Handling**: Use the `multer` library for handling `multipart/form-data`. Ensure the system verifies the file type against the allowed formats.
- **Resume Parsing**: Integrate a resume parsing library (e.g., `resumepdf-parser`) to extract data from uploaded resumes.
- **Security**: Implement file size limitations and virus scanning mechanisms using `ClamAV` to prevent harmful files from being uploaded.
- **Database**: Store resume metadata and extracting data in a PostgreSQL database to maintain candidate information.
- **Testing**: Create unit and integration tests using frameworks like Jest and Supertest to ensure functionality and reliability.
