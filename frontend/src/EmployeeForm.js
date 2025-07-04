import React, { useState } from 'react';

const API_URL = process.env.REACT_APP_API_URL;

function EmployeeForm() {
  const [formData, setFormData] = useState({
    name: '',
    department: '',
    email: '',
    phone: ''
  });

  const handleChange = e => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = e => {
    e.preventDefault();
    fetch(`${API_URL}/employees`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(formData)
    })
      .then(response => response.json())
      .then(data => {
        console.log('Employee updated:', data);
      })
      .catch(error => console.error('Error updating employee:', error));
  };

  return (
    <form onSubmit={handleSubmit}>
      <input name="name" value={formData.name} onChange={handleChange} placeholder="Name" required />
           <input name="email" value={formData.email} onChange={handleChange} placeholder="Email" required />
      <input name="phone" value={formData.phone} onChange={handleChange} placeholder="Phone" required />
      <button type="submit">Update Info</button>
    </form>
  );
}

export default EmployeeForm;
