import Layout from "components/Layout";
import React from "react";
import SearchBox from "components/SearchBox";

const Contact = ({ id }) => {
    return (
        <div id={id} className="min-h-screen w-full mt-10">
            <h1 className="text-4xl text-center m-5">소문난호텔</h1>
            <SearchBox />
        </div>
    );
};

export default Contact;
