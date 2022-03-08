import React from "react";
import Keyboard from "components/img_src/keyboard.svg";

const Footer = () => {
    return (
        // <div classNameName="bg-theme w-screen flex justify-center text-white">
        //     <h1>Developed by 2게된다고? Team</h1>
        // </div>
        <footer className="footer items-center p-3 text-[#222222]  bg-[#F7F7F7] font-notoSans justify-end">
            <div className="items-center grid-flow-col">
                <img className="w-9 h-9" src={Keyboard} alt="footer-logo"></img>
                <p>Developed by 2게된다고?</p>
            </div>
            <div className="grid-flow-col gap-4 md:place-self-center md:justify-self-end justify-end"></div>
        </footer>
    );
};

export default Footer;
