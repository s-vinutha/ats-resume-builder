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

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const resumeResponse = await generateResume(formData);
      console.log("Resume API:", resumeResponse);

      const atsResponse = await getATSScore({
        resume: JSON.stringify(formData),
        jobDescription: formData.jobDescription
      });

      console.log("ATS Score:", atsResponse);
    } catch (error) {
      console.error("API Error:", error);
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
    </form>
  );
}

export default ResumeForm;
