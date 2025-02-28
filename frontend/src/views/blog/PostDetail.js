import React, { Component } from "react";
import withRouter from "helpers/WithRouter";
import moment from 'moment';
import { ServiceFactory } from 'services';
import { withTranslation } from 'react-i18next';
import Spinner from "views/spinner/Spinner";

import Prism from "prismjs";
import "prismjs/themes/prism-tomorrow.min.css";
import "prismjs/plugins/toolbar/prism-toolbar.min.css";
import "prismjs/plugins/toolbar/prism-toolbar.min";
import "prismjs/plugins/show-language/prism-show-language.min.js";
import "prismjs/plugins/line-numbers/prism-line-numbers.min.css";
import "prismjs/plugins/line-numbers/prism-line-numbers.min";
import "prismjs/plugins/copy-to-clipboard/prism-copy-to-clipboard.min";
import "prismjs/plugins/line-highlight/prism-line-highlight.min.css";
import "prismjs/plugins/line-highlight/prism-line-highlight.min.js";
import "prismjs/plugins/command-line/prism-command-line.min.css";
import "prismjs/plugins/command-line/prism-command-line.min.js";

import "prismjs/components/prism-python.min.js";
import "prismjs/components/prism-apacheconf.min.js";
import "prismjs/components/prism-bash.min.js";
import "prismjs/components/prism-json.min.js";
import "prismjs/components/prism-c";
import "prismjs/components/prism-autohotkey.min.js";
import "prismjs/components/prism-autoit.min.js";
import "prismjs/components/prism-awk.min.js";
import "prismjs/components/prism-basic.min.js";
import "prismjs/components/prism-batch.min.js";
import "prismjs/components/prism-cmake.min.js";
import "prismjs/components/prism-c.min.js";
import "prismjs/components/prism-cpp.min.js";
import "prismjs/components/prism-csharp.min.js";
import "prismjs/components/prism-css-extras.min.js";
import "prismjs/components/prism-css.min.js";
import "prismjs/components/prism-csv.min.js";
import "prismjs/components/prism-diff.min.js";
import "prismjs/components/prism-d.min.js";
import "prismjs/components/prism-dns-zone-file.min.js";
import "prismjs/components/prism-docker.min.js";
import "prismjs/components/prism-eiffel.min.js";
import "prismjs/components/prism-elixir.min.js";
import "prismjs/components/prism-excel-formula.min.js";
import "prismjs/components/prism-git.min.js";
import "prismjs/components/prism-go.min.js";
import "prismjs/components/prism-go-module.min.js";
import "prismjs/components/prism-haml.min.js";
import "prismjs/components/prism-haskell.min.js";
import "prismjs/components/prism-http.min.js";
import "prismjs/components/prism-icon.min.js";
import "prismjs/components/prism-ignore.min.js";
import "prismjs/components/prism-ini.min.js";
import "prismjs/components/prism-javadoclike.min.js";
import "prismjs/components/prism-java.min.js";
import "prismjs/components/prism-javascript.min.js";
import "prismjs/components/prism-js-extras.min.js";
import "prismjs/components/prism-json5.min.js";
import "prismjs/components/prism-json.min.js";
import "prismjs/components/prism-jsonp.min.js";
import "prismjs/components/prism-js-templates.min.js";
import "prismjs/components/prism-jsx.min.js";
import "prismjs/components/prism-kotlin.min.js";
import "prismjs/components/prism-lisp.min.js";
import "prismjs/components/prism-log.min.js";
import "prismjs/components/prism-makefile.min.js";
import "prismjs/components/prism-markdown.min.js";
import "prismjs/components/prism-markup.min.js";
import "prismjs/components/prism-markup-templating.min.js";
import "prismjs/components/prism-mongodb.min.js";
import "prismjs/components/prism-n4js.min.js";
import "prismjs/components/prism-nginx.min.js";
import "prismjs/components/prism-puppet.min.js";
import "prismjs/components/prism-python.min.js";
import "prismjs/components/prism-regex.min.js";
import "prismjs/components/prism-r.min.js";
import "prismjs/components/prism-ruby.min.js";
import "prismjs/components/prism-sass.min.js";
import "prismjs/components/prism-scheme.min.js";
import "prismjs/components/prism-scss.min.js";
import "prismjs/components/prism-shell-session.min.js";
import "prismjs/components/prism-smarty.min.js";
import "prismjs/components/prism-sql.min.js";
import "prismjs/components/prism-systemd.min.js";
import "prismjs/components/prism-textile.min.js";
import "prismjs/components/prism-tsx.min.js";
import "prismjs/components/prism-uri.min.js";
import "prismjs/components/prism-vim.min.js";
import "prismjs/components/prism-wiki.min.js";


class PostDatailComponent extends Component {

  constructor(props) {
    super(props)
    this.state = {
      isLoaded: false,
      model: null,
    }
  }

  componentDidMount() {
    this.loadPostModel(this.props.params.slug);
  }

  componentDidUpdate() {
    Prism.highlightAll();
  }

  loadPostModel(slug) {
    var blogService = ServiceFactory.createBlogService();
    blogService.getPost(slug).then(models => {
      if (models.length <= 0) {
        this.setState({
          isLoaded: true,
        });
        return;
      }
      this.setState({
        isLoaded: true,
        model: models[0],
      });
      Prism.highlightAll();
    }).catch(err => {
      alert(err);
    });
  }

  handleOnClickNextPrev(slug) {
    this.setState({
      isLoaded: false,
    });
    this.loadPostModel(slug);
    window.scrollTo({top: 0, behavior: 'smooth'});
  }

  render() {
    if(this.state.isLoaded !== true) {
      return (
        <Spinner/>
      )
    }
    if(this.state.model === null) {
      return (
        <div>
          <div className="text-center text-white">
            <h3 className="font-bold">
              {this.props.t("POST NOT FOUND !")}
            </h3>
            <p className="mt-4 mb-4 font-bold">
              {this.props.t("YOU SEEM TO BE TRYING TO FIND HIS WAY HOME")}
            </p>
            <a href="/" className="bg-pink-700 hover:bg-pink-800 focus:ring-4 focus:ring-pink-300 font-medium rounded-md text-sm px-5 py-2.5 mr-2 mb-2 dark:bg-pink-600 dark:hover:bg-pink-700 focus:outline-none dark:focus:ring-pink-800">
              <span className="font-bold">{this.props.t("Back to home")}</span>
            </a>
          </div>
        </div>
      )
    }
    return (
      <>
        <div className='bg-white shadow-lg rounded-lg lg:p-8 pb-12 mb-8'>
          <div className='relative overflow-hidden shadow-md mb-6'>
            <img
              src={this.state.model.image}
              alt={this.state.model.title}
              decoding='async'
              loading='async'
              fetchpriority='low'
              className="object-top h-full w-full rounded-t-lg"
            />
          </div>
          <div className='px-4 lg:px-0'>
            <div className='flex items-center mb-8 w-full'>
              <div className='font-medium text-gray-700'>
                <svg xmlns="https://www.w3.org/2000/svg" className="h-6 w-6 inline mr-2 text-pink-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
                </svg>
                <span>
                  {moment(this.state.model.publish_date).format('YYYY年 M月 D日')}
                </span>
              </div>
            </div>
            <h1 className='mb-8 text-3xl font-semibold'>{this.state.model.title}</h1>
            <div dangerouslySetInnerHTML={{__html: this.state.model.content}} />
          </div>
        </div>
        <div className="grid grid-cols-1 lg:grid-cols-8 gap-12 mb-8">
          {this.state.model.prev.slug !== "" ?
           <div className="col-span-1 lg:col-span-4 adjacent-post rounded-lg relative h-72">
             <div className="absolute rounded-lg bg-center bg-no-repeat bg-cover shadow-md inline-block w-full h-72"
                  style={{backgroundImage: "url(" + process.env.REACT_APP_API_URL + this.state.model.prev.image + ")"}}></div>
             <div className="absolute rounded-lg bg-center bg-gradient-to-b opacity-50 from-gray-400 via-gray-700 to-black w-full h-72"></div>
             <div className="flex flex-col rounded-lg p-4 items-center justify-center absolute w-full h-full">
               <p className="text-white text-shadow font-semibold text-xs">{moment(this.state.model.prev.publish_date).format('YYYY年 M月 D日')}</p>
               <p className="text-white text-shadow font-semibold text-2xl text-center">{this.state.model.prev.title}</p>
             </div>
             <span className="z-10 cursor-pointer absolute w-full h-full" onClick={() => this.handleOnClickNextPrev(this.state.model.prev.slug)}></span>
             <div className="absolute arrow-btn bottom-5 text-center py-3 cursor-pointer bg-pink-600 left-4 rounded-full">
               <svg xmlns="https://www.w3.org/2000/svg" className="h-6 w-6 text-white w-full" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                 <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"></path>
               </svg>
             </div>
           </div>
           : <div></div>}
          {this.state.model.next.slug !== "" ?
           <div className="col-span-1 lg:col-span-4 adjacent-post rounded-lg relative h-72">
             <div className="absolute rounded-lg bg-center bg-no-repeat bg-cover shadow-md inline-block w-full h-72"
                  style={{backgroundImage: "url(" + process.env.REACT_APP_API_URL + this.state.model.next.image + ")"}}></div>
             <div className="absolute rounded-lg bg-center bg-gradient-to-b opacity-50 from-gray-400 via-gray-700 to-black w-full h-72"></div>
             <div className="flex flex-col rounded-lg p-4 items-center justify-center absolute w-full h-full">
               <p className="text-white text-shadow font-semibold text-xs">{moment(this.state.model.next.publish_date).format('YYYY年 M月 D日')}</p>
               <p className="text-white text-shadow font-semibold text-2xl text-center">{this.state.model.next.title}</p>
             </div>
             <span className="z-10 cursor-pointer absolute w-full h-full" onClick={() => this.handleOnClickNextPrev(this.state.model.next.slug)}></span>
             <div className="absolute arrow-btn bottom-5 text-center py-3 cursor-pointer bg-pink-600 right-4 rounded-full">
               <svg xmlns="https://www.w3.org/2000/svg" className="h-6 w-6 text-white w-full" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                 <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path>
               </svg>
             </div>
           </div>
           : <div></div>}
        </div>
      </>
    )
  }
}
export default withRouter(withTranslation()(PostDatailComponent));
