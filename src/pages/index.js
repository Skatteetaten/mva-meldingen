import React from "react";
import Grid from "@skatteetaten/frontend-components/Grid";
import { SingleColumnRow } from "../components/Columns";
import { graphql } from 'gatsby';

const IndexPage = ({
  data: {
    allMarkdownRemark: { edges },
  },
}) => {
  const FrontPageContent = ({ path }) => {
    const content = edges.find((edge) => {
      return edge.node.fields.slug === path;
    });
    return (
      content && <div dangerouslySetInnerHTML={{ __html: content.node.html }} />
    );
  };

  return (
    <div>
      <Grid>
        <InfoRow>
          <FrontPageContent path="/frontpage/index/" />
        </InfoRow>
      </Grid>

    </div>
  );
};

export default IndexPage;

export const pageQuery = graphql`
  query IndexQuery {
    allMarkdownRemark(filter: {fields: {slug: {eq: "/frontpage/"}}}) {
      edges {
        node {
          id
          html
          fields {
            slug
          }
        }
      }
    }
  }
`;
