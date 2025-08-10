// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0
import React from 'react';

import BarChart from '@cloudscape-design/components/bar-chart';
import Header from '@cloudscape-design/components/header';
import Link from '@cloudscape-design/components/link';

import { WidgetConfig } from '../interfaces';

function DiagramHeader() {
  return (
    <Header variant="h2" description="Your intended diagram?">
        Diagram
    </Header>
  );
}

function DiagramContent() {
  return (
    <div>
        Content!
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