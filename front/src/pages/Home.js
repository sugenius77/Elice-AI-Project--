import React, { useState } from "react";
import Layout from "components/Layout";
import Contact from "./Contact";

const Home = () => {
    return (
        <Layout>
            <Contact />
            <div id="1" className="">
                <div className=" mx-20 items-center mt-20">
                    <h1 className="text-2xl md:text-xl mt-5 md:mt-0">
                        Hello world
                        <b className="text-red-400">Developer</b>
                    </h1>
                </div>
            </div>
        </Layout>
    );
};

export default Home;
