import React from "react";
import Grid from "@skatteetaten/frontend-components/Grid";
import NavigationTile from "@skatteetaten/frontend-components/NavigationTile";
import SkeBasis from "@skatteetaten/frontend-components/SkeBasis";
import { SingleColumnRow } from "../components/Columns";
import { graphql, Link } from "gatsby";

const OmvendtPage = ({
  data: {
    allMarkdownRemark: { edges },
    site: { pathPrefix },
  },
}) => {
  const prefix = process.env.NODE_ENV !== "production" ? "" : pathPrefix;
  const contents = edges
    .filter(
      ({ node }) => node.fields && node.fields.slug.search("/omvendt/") >= 0
    )
    .map(({ node }) => ({
      to: `${prefix}${node.fields.slug}`,
      icon: node.frontmatter.icon,
      heading: node.frontmatter.title,
      description: node.frontmatter.description || "",
    }));

  return (
    <SkeBasis>
      <Grid>
        <SingleColumnRow>
          <a href="https://skatteetaten.github.io/mva-meldingen/omvendt_eng/">
            English
          </a>
          <h3>
            Vi oppdaterer dokumentasjonen med ny struktur og informasjon om
            omvendt avgiftsplikt - feil og døde lenker kan forekomme
          </h3>
          <h1>Dokumentasjon omvendt avgiftsplikt</h1>
        </SingleColumnRow>
        <SingleColumnRow>
          <NavigationTile
            contents={contents}
            renderContent={(to, content) => <Link to={to}>{content}</Link>}
          />
        </SingleColumnRow>
      </Grid>
    </SkeBasis>
  );
};

export default OmvendtPage;

export const pageQuery = graphql`
  query OmvendtQuery {
    site {
      pathPrefix
    }
    allMarkdownRemark(sort: { order: ASC, fields: [frontmatter___title] }) {
      edges {
        node {
          fields {
            slug
          }
          frontmatter {
            title
            icon
            description
          }
        }
      }
    }
  }
`;
