import React from 'react'
import StudentData from './studentData.js'

const StudentEnrolledTable = () => {
  return (
    <div className ="table-container">
      <div className ="table">
 /*         <ul className="student-list">
            <li> Hello </li>
            <li> Bonjour </li>
            <li> Je suis desole </li>
            <li> vous avez un pan</li>
          </ul>*/
         <StudentData />
      </div> 
    </div>
  )
} 
export default StudentEnrolledTable;

