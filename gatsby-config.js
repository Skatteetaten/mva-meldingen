const gatsbyConfig = {
  siteMetadata: {
    title: "Mva-meldingen",
    menu: [
      {
        href: "/",
        name: "Mva-meldingen",
      },
      {
        href: "/documentation",
        name: "Dokumentasjon",
      },
      {
        href: "/frontpage_eng",
        name: "Frontpage in English",
      },
      {
        href: "/english",
        name: "Documentation in English",
      },
    ],
  },
  pathPrefix: "/mva-meldingen",
  plugins: [
    "gatsby-plugin-react-helmet",
    {
      resolve: `gatsby-source-filesystem`,
      options: {
        path: `${__dirname}/docs`,
        name: "markdown-pages",
      },
    },
    {
      resolve: `gatsby-transformer-remark`,
      options: {
        plugins: [
          `gatsby-remark-prismjs`,
          `gatsby-remark-autolink-headers`,
          {
            resolve: "gatsby-remark-copy-linked-files",
            options: {
              // `ignoreFileExtensions` defaults to [`png`, `jpg`, `jpeg`, `bmp`, `tiff`]
              // as we assume you'll use gatsby-remark-images to handle
              // images in markdown as it automatically creates responsive
              // versions of images.
              //
              // If you'd like to not use gatsby-remark-images and just copy your
              // original images to the public directory, set
              // `ignoreFileExtensions` to an empty array.
              ignoreFileExtensions: [],
            },
          },
        ],
      },
    },
  ],
};

module.exports = gatsbyConfig;
