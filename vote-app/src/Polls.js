import '../node_modules/bootstrap/dist/css/bootstrap.min.css';
import React, { Component } from 'react';
// import logo from './logo.svg';
import './App.css';
import Listing from './Listing'
class App extends Component {
    render() {
        return (
            <div className="App">
                <Listing />
            </div>
        );
    }
}

export default App;
