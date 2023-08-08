import React, { Component } from "react";
import { withTranslation } from 'react-i18next';


class Error404 extends Component {

  render() {
    return (
      <div>
        <div className="text-center text-white">
          <h1 className="font-extrabold">
            404
          </h1>
          <h3 className="font-bold">
            {this.props.t("PAGE NOT FOUND !")}
          </h3>
          <p className="mt-4 mb-4 font-bold">
            {this.props.t("YOU SEEM TO BE TRYING TO FIND HIS WAY HOME")}
          </p>
          <a href="/" className="bg-pink-700 hover:bg-pink-800 focus:ring-4 focus:ring-pink-300 font-medium rounded-md text-sm px-5 py-2.5 mr-2 mb-2 dark:bg-pink-600 dark:hover:bg-pink-700 focus:outline-none dark:focus:ring-pink-800">
            <span className="font-bold">{this.props.t("Back to home")}</span>
          </a>
        </div>
      </div>
    );
  };
}
export default withTranslation()(Error404);
