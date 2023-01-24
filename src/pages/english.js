import React from "react";
import Grid from "@skatteetaten/frontend-components/Grid";
import NavigationTile from "@skatteetaten/frontend-components/NavigationTile";
import SkeBasis from "@skatteetaten/frontend-components/SkeBasis";
import { SingleColumnRow } from "../components/Columns";
import { graphql, Link } from "gatsby";

const EnglishPage = ({
  data: {
    allMarkdownRemark: { edges },
    site: { pathPrefix },
  },
}) => {
  const prefix = process.env.NODE_ENV !== "production" ? "" : pathPrefix;
  const contents = edges
    .filter(
      ({ node }) => node.fields && node.fields.slug.search("/english/") >= 0
    )
    .map(({ node }) => ({
      to: `${prefix}${node.fields.slug}`,
      icon: node.frontmatter.icon,
      heading: node.frontmatter.title,
      description: node.frontmatter.description || "",
    }));

  const contents_vat = edges
    .filter(
      ({ node }) =>
        node.fields && node.fields.slug.search("/mvameldingen_eng/") >= 0
    )
    .map(({ node }) => ({
      to: `${prefix}${node.fields.slug}`,
      icon: node.frontmatter.icon,
      heading: node.frontmatter.title,
      description: node.frontmatter.description || "",
    }));

  const contents_compensation = edges
    .filter(
      ({ node }) =>
        node.fields && node.fields.slug.search("/kompensasjon_eng/") >= 0
    )
    .map(({ node }) => ({
      to: `${prefix}${node.fields.slug}`,
      icon: node.frontmatter.icon,
      heading: node.frontmatter.title,
      description: node.frontmatter.description || "",
    }));

  const contents_reverse = edges
    .filter(
      ({ node }) => node.fields && node.fields.slug.search("/omvendt_eng/") >= 0
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
          <h1 id="top"> English documentation </h1>
          <h3>Table of contents</h3>
          <li>
            <a href="#common_documentation"> Common documentation </a>
          </li>
          <li>
            <a href="#vat_report"> Documentation VAT Report </a>
          </li>
          <li>
            <a href="#vat_compensation"> Documentation VAT Compensation </a>
          </li>
          <li>
            <a href="#reverse_tax"> Documentation Reverse Tax Liability</a>
          </li>
        </SingleColumnRow>
        <SingleColumnRow>
          <h2 id="common_documentation">Common documentation</h2>
          <NavigationTile
            contents={contents}
            renderContent={(to, content) => <Link to={to}>{content}</Link>}
          />
          <a href="#top">Return to top</a> |{" "}
          <a href="https://skatteetaten.github.io/mva-meldingen/documentation/">
            Norwegian
          </a>
        </SingleColumnRow>
        <SingleColumnRow>
          <h2 id="vat_report">Documentation VAT report</h2>
          <NavigationTile
            contents={contents_vat}
            renderContent={(to, content) => <Link to={to}>{content}</Link>}
          />
          <a href="#top">Return to top</a> |{" "}
          <a href="https://skatteetaten.github.io/mva-meldingen/mvameldingen/">
            Norwegian
          </a>
        </SingleColumnRow>
        <SingleColumnRow>
          <h2 id="vat_compensation">Documentation VAT Compensation</h2>
          <NavigationTile
            contents={contents_compensation}
            renderContent={(to, content) => <Link to={to}>{content}</Link>}
          />
          <a href="#top">Return to top</a> |{" "}
          <a href="https://skatteetaten.github.io/mva-meldingen/kompensasjon/">
            Norwegian
          </a>
        </SingleColumnRow>
        <SingleColumnRow>
          <h2 id="reverse_tax">Documentation Reverse Tax Liability</h2>
          <h3>
            We are updating our documentation with new structure and information
            about Reverse Tax Liability.
          </h3>
          <NavigationTile
            contents={contents_reverse}
            renderContent={(to, content) => <Link to={to}>{content}</Link>}
          />
          <a href="#top">Return to top</a> |{" "}
          <a href="https://skatteetaten.github.io/mva-meldingen/omvendt/">
            Norwegian
          </a>
        </SingleColumnRow>
      </Grid>
    </SkeBasis>
  );
};

export default EnglishPage;

export const pageQuery = graphql`
  query EnglishQuery {
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
