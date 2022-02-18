import React, { useState } from "react";
import Layout from "components/Layout";
import Contact from "./Contact";

import { useRecoilState } from "recoil";
import { searchResultState } from "state/atom";

const Home = () => {
    const [result, setResult] = useRecoilState(searchResultState);

    return (
        <Layout>
            <Contact />
            <div id="1" className="min-h-screen">
                <div className="h-screen mx-20 items-center mt-20">
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
