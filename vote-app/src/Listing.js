import { Component } from 'react';


class Listing extends Component {

    constructor(props) {
        super(props)
        this.state = {
            records: []
        }

    }

    componentDidMount() {
        fetch('http://192.168.0.132:8700/poll')
            .then(response => response.json())
            .then(records => {
                this.setState({
                    records: records
                })
            })
            .catch(error => console.log(error))
    }

    renderListing() {
        let recordList = []
        this.state.records.map(record => {
            return recordList.push(<li key={record.id}>{record.title}{record.description}{record.options[0]}</li>)
        })

        return recordList;
    }

    render() {
        return (
            <ul>
                {this.renderListing()}
            </ul>
        );
    }
}

export default Listing;