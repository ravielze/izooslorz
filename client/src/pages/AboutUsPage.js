import React, { Component } from "react";

import Image from "../img/logo.jpg";
import Viel from "../img/Viel.jpg";
import Kinan from "../img/Kinan.jpg";
import Kaer from "../img/Kaer.jpg";
import Button from "@material-ui/core/Button";
import NavBar from "../components/NavBar";

const AboutUsPage = () => {
  return (
    <div>
      <NavBar />
      <div className="Container">
        <br></br>
        <div className="HowToUse">
          <img src={Image}></img>
          <div className="HowToUseRight">
            <h2>How to Use</h2>
            <p>
              Uploadlah dokumen terlebih dahulu. Proses upload dokumen dapat dilakukan
              dengan mengklik tombol upload pada home page. Tombol tersebut akan
              menredirect user ke halaman upload. Tekanlah tombol choose file dan
              pilihlah file yang akan diupload. Cara upload juga bisa dilakukan dengan
              cara drag and drop. Setelah memastikan file yang terpilih benar, tekan
              tombol upload maka dokumen akan secara otomatis tersimpan dan siap untuk
              digunakan. Tekanlah tombol back untuk kembali ke home page. Ketiklah
              query pada search bar, dan tekan enter untuk melakukan search.
            </p>
          </div>
          <br></br>
        </div>
        <h2>About Us</h2>
        <div className="developers">
          <div className="member">
            <img src={Viel} style={{width:200}}></img>
            <div className="memberRight">
              <div className="memberName">
                <p style={{fontSize:20}}>Steven Nataniel Kodyat </p>
              </div>
              <p>13519002 </p>
              <p>Teknik Informatika ITB</p>
              <p>Jakarta</p>
              <p>Motto : </p>
            </div>
          </div>
          <div className="member">
            <img src={Kinan} style={{width:200}}></img>
            <div className="memberRight">
              <div className="memberName">
                <p style={{fontSize:20}}>Kinantan Arya Bagaspati</p>
              </div>
              <p>13519044</p>
              <p>Teknik Informatika ITB</p>
              <p>Purwokerto</p>
              <p>Selama janur kuning belum melengkung,</p>
              <p>masih bisa ditikung.</p>
            </div>
          </div>
          <div className="member">
            <img src={Kaer} style={{width:200}}></img>
            <div className="memberRight">
              <div className="memberName">  
                <p style={{fontSize:20}}>Kevin Ryan</p>
              </div>
              <p>13519191</p>
              <p>Teknik Informatika ITB</p>
              <p>Medan</p>
              <p>Motto : Wubbalubbadubdub</p>
            </div>
          </div>
        </div>
        <br></br>
      </div>
    </div>
  );
};
export default AboutUsPage;
