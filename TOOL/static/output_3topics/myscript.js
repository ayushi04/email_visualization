  (function() {
    var fn = function() {
      Bokeh.safely(function() {
        (function(root) {
          function embed_document(root) {
            
          var docs_json = '{"6583224f-4632-43a2-b975-d516b5a14265":{"roots":{"references":[{"attributes":{},"id":"ce2e2595-151a-47a8-bd90-35f31e8f6756","type":"HelpTool"},{"attributes":{},"id":"05eebeb4-3b80-4de2-bb7f-b3fd28b04d93","type":"ResetTool"},{"attributes":{"source":{"id":"6b759ab7-498d-49ed-b817-c8d710c28835","type":"ColumnDataSource"}},"id":"dc86759b-c682-4fae-b26e-e40e8cae99b2","type":"CDSView"},{"attributes":{"fill_alpha":{"value":0.1},"fill_color":{"value":"#1f77b4"},"line_alpha":{"value":0.1},"line_color":{"value":"#1f77b4"},"top":{"field":"top"},"width":{"value":0.9},"x":{"field":"x"}},"id":"e287f839-77d2-4698-b865-7247a5590ce0","type":"VBar"},{"attributes":{"below":[{"id":"54860b2c-4b55-4016-b394-b864752d361a","type":"CategoricalAxis"}],"left":[{"id":"2a939e00-090f-4aa4-8e33-572ba00fa219","type":"LinearAxis"}],"plot_height":250,"renderers":[{"id":"54860b2c-4b55-4016-b394-b864752d361a","type":"CategoricalAxis"},{"id":"82059ed6-8e0e-4af0-a05d-6dbadade49ba","type":"Grid"},{"id":"2a939e00-090f-4aa4-8e33-572ba00fa219","type":"LinearAxis"},{"id":"9561b827-2dc8-403b-803f-7aed61571b3d","type":"Grid"},{"id":"00fa6c61-d94d-47b2-a766-24cf9e5d7fe8","type":"BoxAnnotation"},{"id":"ed1b2794-e695-4452-b2b3-0f908a452421","type":"GlyphRenderer"}],"title":{"id":"090349f8-1719-4fa0-a2fa-97afe58f14c2","type":"Title"},"toolbar":{"id":"88d80bf9-78a8-47cf-91c8-656458bf0aed","type":"Toolbar"},"x_range":{"id":"b3d19035-1d32-4599-b9e5-243bb20645b6","type":"FactorRange"},"x_scale":{"id":"6068da99-5edf-4c43-bc8d-88611dc6763e","type":"CategoricalScale"},"y_range":{"id":"32bd26a5-323a-4651-81e2-e5e5d78ffb98","type":"DataRange1d"},"y_scale":{"id":"bc838a96-caaf-496e-9b9f-bf2568705721","type":"LinearScale"}},"id":"a8766a7f-d15e-47dc-b46a-4a954398d51c","subtype":"Figure","type":"Plot"},{"attributes":{},"id":"6068da99-5edf-4c43-bc8d-88611dc6763e","type":"CategoricalScale"},{"attributes":{"formatter":{"id":"324bb05b-5ff0-4d92-9e99-590c6ca6b0a5","type":"BasicTickFormatter"},"plot":{"id":"a8766a7f-d15e-47dc-b46a-4a954398d51c","subtype":"Figure","type":"Plot"},"ticker":{"id":"7cb02dc6-0491-4deb-83cd-95e6c7984cd7","type":"BasicTicker"}},"id":"2a939e00-090f-4aa4-8e33-572ba00fa219","type":"LinearAxis"},{"attributes":{"formatter":{"id":"d5dec23a-7ffe-454a-be78-667fee999fb6","type":"CategoricalTickFormatter"},"plot":{"id":"a8766a7f-d15e-47dc-b46a-4a954398d51c","subtype":"Figure","type":"Plot"},"ticker":{"id":"493e1e04-33c3-44d5-a4b1-d3a4eaedb9e1","type":"CategoricalTicker"}},"id":"54860b2c-4b55-4016-b394-b864752d361a","type":"CategoricalAxis"},{"attributes":{"callback":null,"factors":["Apples","Pears","Nectarines","Plums","Grapes","Strawberries"]},"id":"b3d19035-1d32-4599-b9e5-243bb20645b6","type":"FactorRange"},{"attributes":{"data_source":{"id":"6b759ab7-498d-49ed-b817-c8d710c28835","type":"ColumnDataSource"},"glyph":{"id":"0eb47896-df57-4a2f-bba1-d0cc19a47b18","type":"VBar"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"e287f839-77d2-4698-b865-7247a5590ce0","type":"VBar"},"selection_glyph":null,"view":{"id":"dc86759b-c682-4fae-b26e-e40e8cae99b2","type":"CDSView"}},"id":"ed1b2794-e695-4452-b2b3-0f908a452421","type":"GlyphRenderer"},{"attributes":{"callback":null,"data":{"top":[5,3,4,2,4,6],"x":["Apples","Pears","Nectarines","Plums","Grapes","Strawberries"]},"selected":{"id":"6c687148-f648-4e56-9ffe-d0c1f1afbd0c","type":"Selection"},"selection_policy":{"id":"8e47d314-0b3c-438e-a18f-7977c469d579","type":"UnionRenderers"}},"id":"6b759ab7-498d-49ed-b817-c8d710c28835","type":"ColumnDataSource"},{"attributes":{},"id":"7644c466-4667-42f3-ad23-403ffa27d1d0","type":"WheelZoomTool"},{"attributes":{"fill_color":{"value":"#1f77b4"},"line_color":{"value":"#1f77b4"},"top":{"field":"top"},"width":{"value":0.9},"x":{"field":"x"}},"id":"0eb47896-df57-4a2f-bba1-d0cc19a47b18","type":"VBar"},{"attributes":{},"id":"bc838a96-caaf-496e-9b9f-bf2568705721","type":"LinearScale"},{"attributes":{},"id":"8e47d314-0b3c-438e-a18f-7977c469d579","type":"UnionRenderers"},{"attributes":{},"id":"534db1dc-d276-44d1-8929-d5cc1b3cca4d","type":"PanTool"},{"attributes":{"callback":null,"start":0},"id":"32bd26a5-323a-4651-81e2-e5e5d78ffb98","type":"DataRange1d"},{"attributes":{},"id":"d6672666-e55c-4123-a382-1b076d60ff0e","type":"SaveTool"},{"attributes":{"dimension":1,"plot":{"id":"a8766a7f-d15e-47dc-b46a-4a954398d51c","subtype":"Figure","type":"Plot"},"ticker":{"id":"7cb02dc6-0491-4deb-83cd-95e6c7984cd7","type":"BasicTicker"}},"id":"9561b827-2dc8-403b-803f-7aed61571b3d","type":"Grid"},{"attributes":{"grid_line_color":{"value":null},"plot":{"id":"a8766a7f-d15e-47dc-b46a-4a954398d51c","subtype":"Figure","type":"Plot"},"ticker":{"id":"493e1e04-33c3-44d5-a4b1-d3a4eaedb9e1","type":"CategoricalTicker"}},"id":"82059ed6-8e0e-4af0-a05d-6dbadade49ba","type":"Grid"},{"attributes":{"overlay":{"id":"00fa6c61-d94d-47b2-a766-24cf9e5d7fe8","type":"BoxAnnotation"}},"id":"9563bdb9-555a-4445-b30c-b5dc7a1828cd","type":"BoxZoomTool"},{"attributes":{"bottom_units":"screen","fill_alpha":{"value":0.5},"fill_color":{"value":"lightgrey"},"left_units":"screen","level":"overlay","line_alpha":{"value":1.0},"line_color":{"value":"black"},"line_dash":[4,4],"line_width":{"value":2},"plot":null,"render_mode":"css","right_units":"screen","top_units":"screen"},"id":"00fa6c61-d94d-47b2-a766-24cf9e5d7fe8","type":"BoxAnnotation"},{"attributes":{"plot":null,"text":"Fruit Counts"},"id":"090349f8-1719-4fa0-a2fa-97afe58f14c2","type":"Title"},{"attributes":{},"id":"6c687148-f648-4e56-9ffe-d0c1f1afbd0c","type":"Selection"},{"attributes":{},"id":"7cb02dc6-0491-4deb-83cd-95e6c7984cd7","type":"BasicTicker"},{"attributes":{},"id":"493e1e04-33c3-44d5-a4b1-d3a4eaedb9e1","type":"CategoricalTicker"},{"attributes":{},"id":"d5dec23a-7ffe-454a-be78-667fee999fb6","type":"CategoricalTickFormatter"},{"attributes":{},"id":"324bb05b-5ff0-4d92-9e99-590c6ca6b0a5","type":"BasicTickFormatter"},{"attributes":{"active_drag":"auto","active_inspect":"auto","active_multi":null,"active_scroll":"auto","active_tap":"auto","tools":[{"id":"534db1dc-d276-44d1-8929-d5cc1b3cca4d","type":"PanTool"},{"id":"7644c466-4667-42f3-ad23-403ffa27d1d0","type":"WheelZoomTool"},{"id":"9563bdb9-555a-4445-b30c-b5dc7a1828cd","type":"BoxZoomTool"},{"id":"d6672666-e55c-4123-a382-1b076d60ff0e","type":"SaveTool"},{"id":"05eebeb4-3b80-4de2-bb7f-b3fd28b04d93","type":"ResetTool"},{"id":"ce2e2595-151a-47a8-bd90-35f31e8f6756","type":"HelpTool"}]},"id":"88d80bf9-78a8-47cf-91c8-656458bf0aed","type":"Toolbar"}],"root_ids":["a8766a7f-d15e-47dc-b46a-4a954398d51c"]},"title":"Bokeh Application","version":"0.13.0"}}';
          var render_items = [{"docid":"6583224f-4632-43a2-b975-d516b5a14265","roots":{"a8766a7f-d15e-47dc-b46a-4a954398d51c":"f31d3ac2-8154-4e3a-a9bd-583dfc5e2484"}}];
          root.Bokeh.embed.embed_items(docs_json, render_items);
        
          }
          if (root.Bokeh !== undefined) {
            embed_document(root);
          } else {
            var attempts = 0;
            var timer = setInterval(function(root) {
              if (root.Bokeh !== undefined) {
                embed_document(root);
                clearInterval(timer);
              }
              attempts++;
              if (attempts > 100) {
                console.log("Bokeh: ERROR: Unable to run BokehJS code because BokehJS library is missing")
                clearInterval(timer);
              }
            }, 10, root)
          }
        })(window);
      });
    };
    if (document.readyState != "loading") fn();
    else document.addEventListener("DOMContentLoaded", fn);
  })();
