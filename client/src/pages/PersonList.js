import React from 'react';
import axios from 'axios';

export default class PersonList extends React.Component {
  state = {
    name: '',
  }

  handleChange = event => {
    this.setState({ name: event.target.value });
  }

  handleSubmit = event => {
    event.preventDefault();

    const search = {
      'keyword': this.state.name,
      'lang': "en"
    };
    console.log(user);
    axios.post(`http://localhost:5000/search`, search)
      .then(res => {
        console.log(res.data.data);
        console.log(res.data.time_in_ms);
        console.log(res.data.termtable);
      })
  }

  render() {
    return (
      <div>
        <form onSubmit={this.handleSubmit}>
          <label>
            Person Name:
            <input type="text" name="name" onChange={this.handleChange} />
          </label>
          <button type="submit">Add</button>
        </form>
      </div>
    )
  }
}