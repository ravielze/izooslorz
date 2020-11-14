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
      <br></br>
      <br></br>
      <br></br>
      <img src={Image}></img>
      <p>
        <h2>How to Use</h2>
        Uploadlah dokumen terlebih dahulu. Proses upload dokumen dapat dilakukan
        dengan mengklik tombol upload pada home page. Tombol tersebut akan
        menredirect user ke halaman upload. Tekanlah tombol choose file dan
        pilihlah file yang akan diupload. Cara upload juga bisa dilakukan dengan
        cara drag and drop. Setelah memastikan file yang terpilih benar, tekan
        tombol upload maka dokumen akan secara otomatis tersimpan dan siap untuk
        digunakan. Tekanlah tombol back untuk kembali ke home page. Ketiklah
        query pada search bar, dan tekan enter untuk melakukan search.
        <br></br>
        <br></br>
        <h2>About Us</h2>
        Pembuat website ini merupakan mahasiswa Teknik Informatika Institut
        Teknologi Bandung angkatan 2019, di antaranya :
        <br></br>
        <img src={Viel}></img>
        <br></br>Nama : Steven Nataniel Kodyat 
        <br></br>NIM : 13519002
        <br></br>Jurusan : Teknik Informatika
        <br></br>Asal Universitas : Institut Teknologi Bandung
        <br></br>Asal Daerah : Jakarta
        <br></br>Motto : 
        <br></br>
        <br></br>
        <img src={Kinan}></img>
        <br></br>Nama : Kinantan Arya Bagaspati
        <br></br>NIM : 13519044
        <br></br>Jurusan : Teknik Informatika
        <br></br>Asal Universitas : Institut Teknologi Bandung
        <br></br>Asal Daerah : Purwokerto
        <br></br>Motto : Selama janur kuning belum melengkung, masih bisa ditikung.
        <br></br>Perkuat pusat perbanyak cabang.
        <br></br>
        <br></br>
        <img src={Kaer}></img>
        <br></br>Nama : Kevin Ryan
        <br></br>NIM : 13519191
        <br></br>Jurusan : Teknik Informatika
        <br></br>Asal Universitas : Institut Teknologi Bandung
        <br></br>Asal Daerah : Medan
        <br></br>Motto : Wubbalubbadubdub
      </p>
      <br></br>
    </div>
  );
};
export default AboutUsPage;
