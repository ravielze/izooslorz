import React, { Component } from 'react';

class Table extends Component {
    constructor(props) {
        super(props)
    }
    renderTableData() {
        return this.props.data.map((termTable, index) => {
            const { terms, query, documents } = termTable
            return (
                <tr key={terms}>
                    <td>{terms}</td>
                    <td>{query}</td>
                    {this.renderTableRow(documents)}
                </tr>
           )
        })
    }
    renderTableRow(props) {
        return props.map((info, index) => {
            return (    
                <td>{info.value}</td>
           )
        })
    }

    renderTableHeader() {
        let header = ['terms', 'query'];
        for(var d=0; d < this.props.data[0].documents.length; d++){
            header.push(this.props.data[0].documents[d]['doc']);
        }
        return header.map((key, index) => {
            return <th key={index}>{key}</th>
        })
    }

    render() {
        return (
            <div>
                <table id='termTable'>
                    <tbody>
                        <tr>{this.renderTableHeader()}</tr>
                        {this.renderTableData()}
                    </tbody>
                </table>
            </div>
        )
    }
}

export default Table;

