foreach [2] + [3] as item
    mailgun send to: ["foo@bar.com"] from: "ss@ss.com" subject: item as string text: "foobar"
