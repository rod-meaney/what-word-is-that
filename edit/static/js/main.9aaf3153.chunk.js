(this["webpackJsonpguess-word-edit"]=this["webpackJsonpguess-word-edit"]||[]).push([[0],{53:function(e,t,a){e.exports=a(68)},58:function(e,t,a){},65:function(e,t,a){},68:function(e,t,a){"use strict";a.r(t);var n=a(1),r=a.n(n),i=a(26),o=a.n(i),s=(a(58),a(11)),l=a(18),c=a(13),u=a(12),m=a(14),h=a(52),p=a(44),d=a(25),b=a(9),f=a(34),g=a(30),v=a(22),E=a(6),O=a(35),y=a(29),k=function(e){function t(e){var a;return Object(s.a)(this,t),(a=Object(c.a)(this,Object(u.a)(t).call(this,e))).handleSubmit=function(e){if(!1===e.currentTarget.checkValidity())e.stopPropagation();else{var t="/edit/api/update";a.props.new&&(t="/edit/api/save"),fetch("https://what-word-is-that.appspot.com"+t,{method:"POST",body:JSON.stringify(a.state)}).then((function(e){return e.json()})).then((function(e){a.setState({saved:!0})}))}a.setState({validated:!0}),e.preventDefault()},a.updateName=function(e){e.preventDefault(),a.setState({name:e.target.value})},a.updateDescription=function(e){e.preventDefault(),a.setState({description:e.target.value})},a.updateItems=function(e){e.preventDefault(),a.setState({items:e.target.value})},a.updatePrivate=function(e){a.setState({private:e.target.checked})},a.state={loaded_id:"",validated:!1,saved:!1,name:"",description:"",items:"",private:!1},a}return Object(m.a)(t,e),Object(l.a)(t,[{key:"componentDidMount",value:function(){if(!this.props.new){var e=window.location.href.split("?id="),t=e[e.length-1],a=this;fetch("".concat("https://what-word-is-that.appspot.com","/").concat("edit","/api/item?id=").concat(t)).then((function(e){return e.json()})).then((function(e){a.setState({loaded_id:t,name:e.name,description:e.description,items:e.items,private:e.private})})).catch((function(e){console.log("Fetch has failed so defaulting in some data for local testing.");var n=!1,r="Cats",i="Purrrrrrrrr",o="Abyssinian,Aegean,American Bobtail,American Curl,American Shorthair,American Wirehair,Aphrodite Giant,Arabian Mau,Asian cat,Asian Semi-longhair,Australian Mist,Balinese,Bambino,Bengal,Birman,Bombay,Brazilian Shorthair,British Longhair,British Shorthair,Burmese,Burmilla,California Spangled,Chantilly-Tiffany,Chartreux,Chausie,Colourpoint Shorthair,Cornish Rex,Cymric,Longhaired Manx,Cyprus,Devon Rex,Donskoy,Don Sphynx,Dragon Li,Dwelf,Egyptian Mau,European Shorthair,Exotic Shorthair,Foldex,German Rex,Havana Brown,Highlander,Himalayan,Japanese Bobtail,Javanese,Khao Manee,Korat,Korean Bobtail,Korn Ja,Kurilian Bobtail\xa0or,Kuril Islands Bobtail,LaPerm,Lykoi,Maine Coon,Manx,Mekong Bobtail,Minskin,Napoleon,Munchkin,Nebelung,Norwegian Forest Cat,Ocicat,Ojos Azules,Oregon Rex,Oriental Bicolor,Oriental Longhair,Oriental Shorthair,Persian,Peterbald,Pixie-bob,Ragamuffin,Ragdoll,Raas,Russian Blue,Russian White,Black,and Tabby,Sam sawet,Savannah,Scottish Fold,Selkirk Rex,Serengeti,Serrade Petit,Siberian,Neva Masquerade,Singapura,Snowshoe,Sokoke,Somali,Sphynx,Suphalak,Thai,Thai Lilac,Tonkinese,Toyger,Turkish Angora,Turkish Van,Ukrainian Levkoy,Wila Krungthep,York Chocolate";a.setState({loaded_id:t,name:r,description:i,items:o,private:n})}))}}},{key:"render",value:function(){return this.state.saved?r.a.createElement(v.a,{to:"/saved"}):r.a.createElement(b.a,null,r.a.createElement(b.a.Body,null,r.a.createElement(E.a,{noValidate:!0,validated:this.state.validated,onSubmit:this.handleSubmit},r.a.createElement(E.a.Row,null,r.a.createElement(y.a,null,r.a.createElement(E.a.Group,{controlId:"formName"},r.a.createElement(E.a.Label,null,"List name"),r.a.createElement(E.a.Control,{placeholder:"eg Simpson characters",required:!0,type:"text",onChange:this.updateName,value:this.state.name}),r.a.createElement(E.a.Control.Feedback,{type:"invalid"},"You must select a name")))),r.a.createElement(E.a.Row,null,r.a.createElement(y.a,null,r.a.createElement(E.a.Group,{controlId:"formDescription"},r.a.createElement(E.a.Label,null,"List description"),r.a.createElement(E.a.Control,{as:"textarea",rows:"2",required:!0,type:"text",onChange:this.updateDescription,value:this.state.description}),r.a.createElement(E.a.Control.Feedback,{type:"invalid"},"A short description helps")))),r.a.createElement(E.a.Row,null,r.a.createElement(y.a,null,r.a.createElement(E.a.Group,{controlId:"formItems"},r.a.createElement(E.a.Label,null,"List items (return or comma)"),r.a.createElement(E.a.Control,{as:"textarea",rows:"4",required:!0,type:"text",onChange:this.updateItems,value:this.state.items}),r.a.createElement(E.a.Control.Feedback,{type:"invalid"},"Add some list words!")))),r.a.createElement(E.a.Row,null,r.a.createElement(E.a.Group,{id:"formPrivate"},r.a.createElement(E.a.Check,{type:"checkbox",checked:this.state.private,label:"Tick to keep list private",onChange:this.updatePrivate}))),r.a.createElement(O.a,{type:"submit"},"Save"))))}}]),t}(r.a.Component),j=function(e){function t(){return Object(s.a)(this,t),Object(c.a)(this,Object(u.a)(t).apply(this,arguments))}return Object(m.a)(t,e),t}(k),w=function(e){function t(){return Object(s.a)(this,t),Object(c.a)(this,Object(u.a)(t).apply(this,arguments))}return Object(m.a)(t,e),t}(k),C=(a(65),a(40)),S=function(e){function t(e){var a;return Object(s.a)(this,t),(a=Object(c.a)(this,Object(u.a)(t).call(this,e))).state={key:a.props.id,description:a.props.description,name:a.props.name,private:a.props.private},a}return Object(m.a)(t,e),Object(l.a)(t,[{key:"render",value:function(){return r.a.createElement(C.a.Item,{action:!0,href:"/item?id=".concat(this.state.key)},this.state.name,r.a.createElement("span",{className:"float-right"},r.a.createElement(f.a,null)))}}]),t}(r.a.Component),B=function(e){function t(e){var a;return Object(s.a)(this,t),(a=Object(c.a)(this,Object(u.a)(t).call(this,e))).state={games:[]},a}return Object(m.a)(t,e),Object(l.a)(t,[{key:"componentDidMount",value:function(){var e=this;fetch("https://what-word-is-that.appspot.com"+"/".concat("edit","/api/").concat(this.props.api)).then((function(e){return e.json()})).then((function(t){e.setState({games:t})})).catch((function(t){console.log("Fetch has failed so defaulting in some data for local testing.");e.setState({games:[{key:"aghkZXZ-Tm9uZXIRCxIETGlzdBiAgICAgICACQw",private:!1,name:"Cats",description:"Purrrrrrrrr"},{key:"aghkZXZ-Tm9uZXIRCxIETGlzdBiAgICAgICACgw",private:!1,name:"Dogs",description:"Doggies"}]})}))}},{key:"noItems",value:function(){return 0===this.state.games.length?r.a.createElement(C.a.Item,null,"Currently no items"):""}},{key:"render",value:function(){return r.a.createElement(b.a,null,r.a.createElement(b.a.Body,null,r.a.createElement(C.a,null,this.state.games.map((function(e){return r.a.createElement(S,{id:e.key,key:e.key,name:e.name,description:e.description,private:e.private})})),this.noItems())))}}]),t}(r.a.Component),I=function(e){function t(e){var a;return Object(s.a)(this,t),(a=Object(c.a)(this,Object(u.a)(t).call(this,e))).state={},a}return Object(m.a)(t,e),Object(l.a)(t,[{key:"render",value:function(){return r.a.createElement(b.a,null,r.a.createElement(b.a.Body,null,r.a.createElement("p",null,"Well Saved!"),this.props.stdOption()))}}]),t}(r.a.Component),A=function(e){function t(){return Object(s.a)(this,t),Object(c.a)(this,Object(u.a)(t).apply(this,arguments))}return Object(m.a)(t,e),Object(l.a)(t,[{key:"render",value:function(){return r.a.createElement(b.a,null,r.a.createElement(b.a.Body,null,r.a.createElement(b.a.Title,null,"Logged in page"),r.a.createElement("p",null,"You are logged in as ",this.props.user,"."),this.props.stdOption()))}}]),t}(r.a.Component),x=function(e){function t(){return Object(s.a)(this,t),Object(c.a)(this,Object(u.a)(t).apply(this,arguments))}return Object(m.a)(t,e),Object(l.a)(t,[{key:"render",value:function(){return r.a.createElement(b.a,null,r.a.createElement(b.a.Body,null,r.a.createElement(b.a.Title,null,"WWIT Admin Home"),r.a.createElement("p",null,"Administration for WWIT (What word is that)"),this.props.stdOption()))}}]),t}(r.a.Component),T=function(e){function t(e){var a;return Object(s.a)(this,t),(a=Object(c.a)(this,Object(u.a)(t).call(this,e))).state={auth:!1,user:"login"},a}return Object(m.a)(t,e),Object(l.a)(t,[{key:"componentDidMount",value:function(){var e=this;fetch("https://what-word-is-that.appspot.com/api/user").then((function(e){return e.json()})).then((function(t){var a=t.response;"anonymous"!==a&&e.setState({auth:!0,user:a})})).catch((function(e){console.log("Fetch user has failed so assume anonymous - do nothing")}))}},{key:"standardOptions",value:function(){return r.a.createElement(r.a.Fragment,null,r.a.createElement(d.a.Item,{as:g.b,to:"/my-lists"},"My lists"),r.a.createElement(d.a.Item,{as:g.b,to:"/create-new-list"},"Create new list"),r.a.createElement(d.a.Item,{href:"../"},"Return to play game"))}},{key:"render",value:function(){return r.a.createElement(g.a,{basename:"/".concat("edit")},r.a.createElement(h.a,null,r.a.createElement(p.a,{bg:"light",expand:"lg"},r.a.createElement(d.a,{title:r.a.createElement(f.b,null),id:"basic-nav-dropdown",className:"nav-item dropdown mr-auto"},this.standardOptions(),r.a.createElement(d.a.Divider,null),r.a.createElement(d.a.Item,null,r.a.createElement(f.c,null)," ",this.state.user)),r.a.createElement(p.a.Brand,{as:g.b,to:"/"},"WWWiT Admin")),r.a.createElement(v.d,null,r.a.createElement(v.b,{path:"/create-new-list"},r.a.createElement(w,{stdOption:this.standardOptions,new:!0})),r.a.createElement(v.b,{path:"/item"},r.a.createElement(j,{stdOption:this.standardOptions,new:!1})),r.a.createElement(v.b,{path:"/my-lists"},r.a.createElement(B,{api:"my-lists"})),r.a.createElement(v.b,{path:"/logged-in"},r.a.createElement(A,{user:this.state.user,stdOption:this.standardOptions})),r.a.createElement(v.b,{path:"/saved"},r.a.createElement(I,{stdOption:this.standardOptions})),r.a.createElement(v.b,{path:"/"},r.a.createElement(x,{stdOption:this.standardOptions})))))}}]),t}(r.a.Component);Boolean("localhost"===window.location.hostname||"[::1]"===window.location.hostname||window.location.hostname.match(/^127(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$/));a(67);o.a.render(r.a.createElement(T,null),document.getElementById("root")),"serviceWorker"in navigator&&navigator.serviceWorker.ready.then((function(e){e.unregister()})).catch((function(e){console.error(e.message)}))}},[[53,1,2]]]);
//# sourceMappingURL=main.9aaf3153.chunk.js.map