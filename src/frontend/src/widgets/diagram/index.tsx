// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0
import React, { useEffect, useRef, useState } from 'react';

import BarChart from '@cloudscape-design/components/bar-chart';
import Header from '@cloudscape-design/components/header';
import Link from '@cloudscape-design/components/link';
import { VegaLite } from 'react-vega';

import { WidgetConfig } from '../interfaces';

function DiagramHeader() {
  return (
    <Header variant="h2" description="Your intended diagram?">
        Diagram
    </Header>
  );
}

function DiagramContent({ jsonSpec }) {
  const containerRef = useRef(null);
  const [specWithSize, setSpecWithSize] = useState({});

  useEffect(() => {
      if (!jsonSpec || Object.keys(jsonSpec).length === 0) {
        setSpecWithSize({});
        return;
      }

      // Calculate size from container or fallback to window
      const width = containerRef.current?.clientWidth || window.innerWidth;
      const height = containerRef.current?.clientHeight || window.innerHeight;

      // Clone jsonSpec and inject width/height
      const newSpec = {
        ...jsonSpec,
        width,
        height,
      };
      setSpecWithSize(newSpec);
  }, [jsonSpec]);

  // jsonSpec is empty ie. no rendering has occurred
  if (!jsonSpec || Object.keys(jsonSpec).length === 0) {
    return <div>No Diagram data available</div>
  }

  return (
    <div ref={containerRef} style={{width: '100%', height: '100%'}}>
      <VegaLite spec={specWithSize} />
    </div>
  );
}
export const diagram: WidgetConfig = {
  definition: { defaultRowSpan: 4, defaultColumnSpan: 2, minRowSpan: 3 },
  data: {
    title: 'Diagram',
    description: 'Diagram',
    header: DiagramHeader,
    content: DiagramContent,
    staticMinHeight: 560,
  },
};