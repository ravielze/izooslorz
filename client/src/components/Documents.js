import React from 'react';


const Document = (props) => {
    const { url, namafile, jumlahkata, kecocokan, firstsentence } = props;
  
    return (
      <div className="docuQueryMap">
        <h2><a href={url}>{namafile}</a></h2>
        <p style={{marginTop: -10}}>Jumlah kata: {jumlahkata} </p>
        <p style={{marginTop: -10}}>Tingkat Kemiripan: {Math.round(100000*kecocokan)/1000}%</p>
        <p style={{marginTop: -10}}>{firstsentence}</p>
      </div>
    );
};

const DocuQuery = (props) => {
    const { data } = props;
    return (
        <div className="Documents">
            {data.map((documents) => (
                <Document key={documents.namafile} {...documents} />
            ))}
        </div>
  );
}
export default DocuQuery;