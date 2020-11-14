import React, { Component } from 'react';


class Table extends Component {
    constructor(props) {
        super(props)
        this.state = {
            termTable: [
                {'terms': 'everlast', 'query': '0', 'documents': [{'doc': '1.txt', 'value': 0},{'doc': '2.txt', 'value': 1},{'doc': '3.txt', 'value': 0}]},
                {'terms': 'game', 'query': '0', 'documents': [{'doc': '1.txt', 'value': 0},{'doc': '2.txt', 'value': 2},{'doc': '3.txt', 'value': 0}]}
            ]
        }
    }
    renderTableData() {
        return this.state.termTable.map((termTable, index) => {
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
        for(var d=0; d < this.state.termTable[0].documents.length; d++){
            header.push(this.state.termTable[0].documents[d]['doc']);
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

