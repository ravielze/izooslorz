import React,{Component} from 'react'; 
  
import Image from "./img/logo.jpg";

const AboutUsPage = () => {

    return(
    <div>
        <img src={Image} className="AboutUsLogo"></img>
        <p className="AboutUsText">
            How to Use
            <br></br>
            Uploadlah dokumen terlebih dahulu. Proses upload dokumen dapat dilakukan dengan mengklik tombol upload pada home page. Tombol tersebut akan menredirect user ke halaman upload. Tekanlah tombol choose file dan pilihlah file yang akan diupload. Cara upload juga bisa dilakukan dengan cara drag and drop. Setelah memastikan file yang terpilih benar, tekan tombol upload maka dokumen akan secara otomatis tersimpan dan siap untuk digunakan. Tekanlah tombol back untuk kembali ke home page. Ketiklah query pada search bar, dan tekan enter untuk melakukan search.
            <br></br>
            <br></br>
            About Us
            <br></br>
            Pembuat website ini merupakan mahasiswa Teknik Informatika Institut Teknologi Bandung angkatan 2019 yang bernama Steven Nataniel Kodyat (13519002), Kinantan Arya Bagaspati (13519044), dan Kevin Ryan (13519191).
        </p>
        <a href="/home">
            <button>
                Back    
            </button>
        </a>
    </div>

    )
} 
export default AboutUsPage