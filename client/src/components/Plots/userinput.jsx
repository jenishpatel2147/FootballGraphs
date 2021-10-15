import React from 'react'

export default class userinput extends React.Component {
    constructor(props) {
      super(props);
      this.state = {value: 'EPL'};
  
      this.handleChange = this.handleChange.bind(this);
      this.handleSubmit = this.handleSubmit.bind(this);
    }
  
    handleChange(event) {
      this.setState({value: event.target.value});
    }
  
    handleSubmit(event) {
      ""
    //alert('Your favorite flavor is: ' + this.state.value);
      event.preventDefault();
    }
  
    render() {
      return (
        <form onSubmit={this.handleSubmit}>
          <label>
            Pick League:
            <select value={this.state.value} onChange={this.handleChange}>
              <option value="england">EPL</option>
              <option value="italy">Serie A</option>
              <option value="germany">Bundesliga</option>
              <option value="spain">La Liga</option>
              <option value="france">Ligue 1</option>
            </select>
          </label>
          <input type="submit" value="Submit" />
        </form>
      );
    }
  }
  