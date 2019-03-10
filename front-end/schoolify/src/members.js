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
      .then(response => response.json())
      .then(data =>this.setState({students: data.students}));
  }

  render() {
    const {students} = this.state;
    return (

      <ul className="member">
        {students.map(student => 
            <li key={student.objectID}>
              <a href="">{student[1]}  {student[2]} </a>
            </li>
        )} 
      </ul>
    );
  }
}

export default Members;
