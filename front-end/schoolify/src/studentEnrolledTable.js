import React from 'react'
import StudentData from './studentData.js'
import Members from './members.js'
const StudentEnrolledTable = () => {
  return (
    <div className ="table-container">
      <div className ="table">
    { /*         <ul className="student-list">
            <li> Hello </li>
            <li> Bonjour </li>
            <li> Je suis desole </li>
            <li> vous avez un pan</li>
          </ul>
         <StudentData />*/}
         <Members />
      </div> 
    </div>
  )
} 
export default StudentEnrolledTable;

