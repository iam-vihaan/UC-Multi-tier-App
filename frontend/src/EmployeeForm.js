import React, { useState } from 'react';

function EmployeeForm() {
  const [formData, setFormData] = useState({
    name: '',
    department: '',
    email: ''
  });

  const handleChange = e => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = e => {
    e.preventDefault();
    fetch('/api/employees', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(formData)
    }).then(() => {
      alert('Employee updated!');
    });
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Update Your Info</h2>
      <input name="name" placeholder="Name" onChange={handleChange} />
      <input name="department" placeholder="Department" onChange={handleChange} />
      <input name="email" placeholder="Email" onChange={handleChange} />
      <button type="submit">Update</button>
    </form>
  );
}

export default EmployeeForm;
