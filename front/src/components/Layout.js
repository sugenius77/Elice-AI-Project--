import React from "react";
import Footer from "components/Footer";

const Layout = ({ children, id }) => {
    return (
        <div id={id}>
            <div className="content overflow-x-hidden">{children}</div>
            <Footer />
        </div>
    );
};

export default Layout;
