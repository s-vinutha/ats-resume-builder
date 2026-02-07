import { useState } from "react";
import { generateResume, getATSScore } from "../api";

function ResumeForm() {
  const [formData, setFormData] = useState({
    name: "",
    email: "",
    phone: "",
    skills: "",
    education: "",
    projects: "",
    experience: "",
    jobDescription: ""
  });

  const [atsScore, setAtsScore] = useState(null);
  const [missingKeywords, setMissingKeywords] = useState([]);

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      // Generate resume PDF
      const pdfBlob = await generateResume(formData);
      const url = window.URL.createObjectURL(pdfBlob);
      const a = document.createElement("a");
      a.href = url;
      a.download = "ATS_Resume.pdf";
      a.click();

      // Get ATS score
      const atsResponse = await getATSScore({
        resume: `
          ${formData.skills}
          ${formData.education}
          ${formData.projects}
          ${formData.experience}
        `,
        jobDescription: formData.jobDescription
      });

      setAtsScore(atsResponse.ats_score);
      setMissingKeywords(atsResponse.missing_keywords);

    } catch (error) {
      console.error("Error during resume generation or ATS scoring", error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>ATS Resume Builder</h2>

      <input name="name" placeholder="Full Name" onChange={handleChange} />
      <input name="email" placeholder="Email" onChange={handleChange} />
      <input name="phone" placeholder="Phone Number" onChange={handleChange} />

      <textarea name="skills" placeholder="Skills" onChange={handleChange} />
      <textarea name="education" placeholder="Education" onChange={handleChange} />
      <textarea name="projects" placeholder="Projects" onChange={handleChange} />
      <textarea name="experience" placeholder="Experience" onChange={handleChange} />

      <textarea
        name="jobDescription"
        placeholder="Paste Job Description"
        onChange={handleChange}
      />

      <button type="submit">Submit</button>

      {/* ✅ ATS SCORE UI MUST BE INSIDE RETURN */}
      {atsScore !== null && (
        <div style={{ marginTop: "20px" }}>
          <h3>ATS Score: {atsScore}%</h3>
          <progress value={atsScore} max="100" />

          {missingKeywords.length > 0 && (
            <>
              <h4>Missing Keywords:</h4>
              <ul>
                {missingKeywords.map((kw, i) => (
                  <li key={i}>{kw}</li>
                ))}
              </ul>
            </>
          )}
        </div>
      )}
    </form>
  );
}

export default ResumeForm;
