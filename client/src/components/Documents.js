import React from 'react';

const allDocuments = [{'Nama_File': '1.txt', 'Jumlah_Kata': '8', 'Tingkat_Kecocokan': 0.3900194645305693, 'Kalimat_Pertama': 'The game of life is a game of everlasting learning'},  
{'Nama_File': '2.txt', 'Jumlah_Kata': '7', 'Tingkat_Kecocokan': 0.2550098061181917, 'Kalimat_Pertama': 'The unexamined life is not worth living'},
{'Nama_File': '3.txt', 'Jumlah_Kata': '3', 'Tingkat_Kecocokan': 0.30263669792912185, 'Kalimat_Pertama': 'Never stop learning'}];

const Document = (props) => {
    const { Nama_File, Jumlah_Kata, Tingkat_Kecocokan, Kalimat_Pertama } = props;
  
    return (
      <div className= "Document-container">
        <h2 className="Document__filename">{Nama_File}</h2>
        <p className= "Document__words" style={{marginTop: -10}}> Jumlah kata: {Jumlah_Kata} </p>
        <p className="Document__similarity" style={{marginTop: -10}}>Tingkat Kemiripan: {Math.round(1000*Tingkat_Kecocokan)/1000}%</p>
        <p className="Document__firstsentence" style={{marginTop: -10}}>{Kalimat_Pertama}</p>
      </div>
    );
};

export default function DocuQuery() {
  return (
    <div className="Documents">
        {allDocuments.map((documents) => (
            <Document key={documents.Nama_File} {...documents} />
        ))}
    </div>
  );
}