import React, { useEffect, useState } from 'react';

const API_URL = process.env.REACT_APP_API_URL;

function EmployeeList() {
  const [employees, setEmployees] = useState([]);

  useEffect(() => {
    fetch(`${API_URL}/employees`)
      .then(response => response.json())
      .then(data => setEmployees(data))
      .catch(error => console.error('Error fetching employees:', error));
  }, []);

  return (
    <div>
      <h2>Employee Directory</h2>
      <ul>
        {employees.map(emp => (
          <li key={emp.id}>{emp.name} - {emp.department}</li>
        ))}
      </ul>
    </div>
  );
}

export default EmployeeList;
