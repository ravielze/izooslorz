import React from 'react';

const allDocuments = [{'Nama_File': '1.txt', 'Jumlah_Kata': '8', 'Tingkat_Kecocokan': 0.3900194645305693, 'Kalimat_Pertama': 'The game of life is a game of everlasting learning'},  
{'Nama_File': '2.txt', 'Jumlah Kata': '7', 'Tingkat_Kecocokan': 0.2550098061181917, 'Kalimat_Pertama': 'The unexamined life is not worth living'},
{'Nama_File': '3.txt', 'Jumlah_Kata': '3', 'Tingkat_Kecocokan': 0.30263669792912185, 'Kalimat_Pertama': 'Never stop learning'}];

const Document = (props) => {
    const { Nama_File, Jumlah_Kata, Tingkat_Kecocokan, Kalimat_Pertama } = props;
  
    return (
      <div className= "Document-container">
        <h4 className="Document__filename">{Nama_File}</h4>
        <h5 className="Document__words">{Jumlah_Kata}</h5>
        <p className="Document__similarity">{Tingkat_Kecocokan}</p>
        <p className="Document__firstsentence">{Kalimat_Pertama}</p>
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