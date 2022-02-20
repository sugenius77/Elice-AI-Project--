import Layout from "components/Layout";
import React from "react";
import SearchBox from "components/SearchBox";

const Contact = ({ id }) => {
    return (
        <div id={id} className="min-h-screen w-full mt-10">
            <h1 className="text-4xl text-center m-5">키보드로 소문난 호텔</h1>
            <SearchBox />
        </div>
    );
};

export default Contact;
