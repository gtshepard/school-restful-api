import React, {Component} from 'react'


const API = 'http://localhost:5000/school/api/v1.0/';
const QUERY = 'students';

class Members extends Component {
  constructor(props) {
    super(props)
      this.state = {
        students:[],
      };
  }

  componentDidMount(){
    fetch(API + QUERY)
      .then(response => console.log(response.json()))
      .then(data => this.setState({students: data.students}));
  }


  render() {
    const {students} = this.state;
    return (
      <ul>
        {students.map(student => 
            <li key={student.objectID}>
               {student[0][0]}              
            </li>
        )} 
      </ul>
    );
  }
}

export default Members;
