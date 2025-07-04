import React, { useEffect, useState } from 'react';

function EmployeeList() {
  const [employees, setEmployees] = useState([]);

  useEffect(() => {
    fetch('/api/employees')
      .then(res => res.json())
      .then(data => setEmployees(data));
  }, []);

  return (
    <div>
      <h2>Employees</h2>
      <ul>
        {employees.map(emp => (
          <li key={emp.id}>
            {emp.name} - {emp.department} - {emp.email}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default EmployeeList;
