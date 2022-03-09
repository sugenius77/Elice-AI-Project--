import React from "react";
import Layout from "../components/Layout";
import Result from "../components/Result";
import About from "../components/About";
import { Link } from "react-scroll";

import SearchBox from "../components/SearchBox";

import AOS from "aos";

import mainVideo from "../components/video_src/main_video.mp4";
import logo from "../components/img_src/logo.jpg";

AOS.init({
    duration: 1000,
});

const Home = () => {
    document.title = "키보드호텔";
    return (
        <>
            <Layout id="1">
                <div className="h-screen">
                    <div className="md:z-20">
                        <video
                            autoPlay
                            loop
                            muted
                            className="w-full absolute object-cover h-screen"
                        >
                            <source src={mainVideo} type="video/mp4" />
                        </video>
                    </div>
                    <div className="h-screen w-full bg-gradient-to-r from-black  opacity-50 z-30 absolute md:hidden lg:hidden"></div>
                    <div className="min-h-screen md:bg-hero md:bg-cover md:bg-center lg:bg-hero lg:bg-cover lg:bg-center lg:w-full absolute md:static z-40">
                        <div className="md:text-center md:w-full relative items-center pt-36 pl-52 md:pl-0 justify-center w-fit flex-col">
                            <h1 className=" text-7xl md:text-5xl pt-20  md:mt-16 mb-5 text-white font-title text-shadow-lg">
                                키보드로
                                <br />
                                소문난
                                <br />
                                호텔
                            </h1>

                            <p className=" mb-5 font-notoSans text-gray-100 text-shadow-lg">
                                🔔무엇을 도와드릴까요?
                            </p>
                            <div className="flex md:justify-center z-40">
                                <Link
                                    to="2"
                                    spy={true}
                                    smooth={true}
                                    className="py-2 px-4 font-semibold rounded-lg shadow-md bg-sub hover:bg-point2 hover:text-white cursor-pointer btn border-0 text-gray-600 md:items-center md:justify-center"
                                >
                                    Check-in
                                </Link>
                            </div>
                        </div>
                    </div>
                </div>
                <About />
                <div id="2" className=" w-full pt-20 bg-primary">
                    {/* <h1 className="text-6xl text-center mb-5 font-semibold text-fontcolor">
                        ⌨
                    </h1> */}
                    <div className="flex justify-center">
                        <img
                            src={logo}
                            alt=""
                            className=" h-28 shadow-lg mb-8"
                        />
                    </div>
                    {/* <h1 className="text-4xl text-center">⌨</h1> */}
                    <SearchBox />
                </div>

                <div>
                    <Result />
                </div>
            </Layout>
        </>
    );
};

export default Home;
