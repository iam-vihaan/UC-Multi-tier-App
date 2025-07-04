import React, { useState } from 'react';
import axios from 'axios';

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
    axios.post(`${API_URL}/employees`, formData)
      .then(response => {
        console.log('Employee updated:', response.data);
      })
      .catch(error => console.error('Error updating employee:', error));
  };

  return (
    <form onSubmit={handleSubmit}>
      <input name="name" value={formData.name} onChange={handleChange} placeholder="Name" required />
      <input name="department" value={formData.department} onChange={handleChange} placeholder="Department" required />
      <input name="email" value={formData.email} onChange={handleChange} placeholder="Email" required />
      <input name="phone" value={formData.phone} onChange={handleChange} placeholder="Phone" required />
      <button type="submit">Update Info</button>
    </form>
  );
}

export default EmployeeForm;
