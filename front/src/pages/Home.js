import React from "react";
import Layout from "components/Layout";
import Result from "components/Result";
import TestResult from "components/testResult";
import { Link } from "react-scroll";

import SearchBox from "components/SearchBox";

import AOS from "aos";

import VideoPlayer from "react-background-video-player";
import mainVideo from "components/img_src/main_video.mp4";

AOS.init({
    duration: 1000,
});

const Home = () => {
    document.title = "키보드호텔";
    return (
        <Layout id="1">
            <VideoPlayer
                className="video md:hidden opacity-70"
                src={mainVideo}
                autoPlay={true}
                muted={true}
                // disableBackgroundCover={true}
            />
            <div className="min-h-screen md:bg-hero md:bg-cover md:bg-center">
                <div className="md:text-center md:w-full relative items-center pt-36 pl-16 md:pl-0 justify-center w-fit flex-col">
                    <h1 className=" text-5xl md:text-xl pt-20  md:mt-0 mb-10 font-bold text-white text-reviewsFont">
                        키보드로 소문난 호텔
                    </h1>
                    <div className="flex justify-center">
                        <Link
                            to="2"
                            spy={true}
                            smooth={true}
                            className="py-2 px-4 font-semibold rounded-lg shadow-md bg-sub hover:bg-point2 hover:text-white cursor-pointer btn border-0 text-gray-600 items-center justify-center"
                        >
                            get started
                        </Link>
                    </div>
                </div>
            </div>

            <div id="2" className=" w-full pt-20 bg-primary">
                <h1 className="text-4xl text-center m-5 font-semibold text-fontcolor">
                    키보드로 소문난 호텔
                </h1>
                <h1 className="text-4xl text-center">⌨</h1>
                <SearchBox />
            </div>

            <div>
                <Result />
                {/* <TestResult></TestResult> */}
            </div>
        </Layout>
    );
};

export default Home;
