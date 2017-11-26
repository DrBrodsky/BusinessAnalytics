import java.io.IOException;

import com.amazonaws.AmazonClientException;
import com.amazonaws.AmazonServiceException;
import com.amazonaws.auth.AWSStaticCredentialsProvider;
import com.amazonaws.auth.BasicAWSCredentials;
import com.amazonaws.auth.profile.ProfileCredentialsProvider;
import com.amazonaws.regions.Regions;
import com.amazonaws.services.s3.AmazonS3;
import com.amazonaws.services.s3.AmazonS3Client;
import com.amazonaws.services.s3.AmazonS3ClientBuilder;
import com.amazonaws.services.s3.model.CopyObjectRequest;

/**
 * Sample class for copying name.basics.tsv.gz from the 'current' folder in the
 * imdb-datasets s3 bucket into your own s3 bucket/folder.
 *
 * Use with AWS Java SDK 1.11.156 or later.
 */
public class CopyObjectSingleOperation {
    private static String srcBucketName  = "imdb-datasets";
    private static String srcKey         = "documents/v1/current/name.basics.tsv.gz";
    private static String desBucketName  = "ucl-dissertation-storage";
    private static String desKey         = "target-folder/name.basics.tsv.gz";

    public static void main(String[] args) throws IOException {

        BasicAWSCredentials creds = new BasicAWSCredentials(Credentials.accessKeyId, Credentials.secretKey);
        AmazonS3 s3client = AmazonS3ClientBuilder.standard().
                withCredentials(new AWSStaticCredentialsProvider(creds)).
                withRegion(Regions.EU_WEST_2).build();

        try {
            // Copying object
            // NOTE: It's necessary to set RequesterPays to true!
            CopyObjectRequest copyObjRequest = new CopyObjectRequest(srcBucketName,
                                                                     srcKey,
                                                                     desBucketName,
                                                                     desKey)
                                                   .withRequesterPays(true);
            System.out.println("Copying object.");
            s3client.copyObject(copyObjRequest);

        } catch (AmazonServiceException ase) {
            System.out.println("Caught an AmazonServiceException, " +
                    "which means your request made it " +
                    "to Amazon S3, but was rejected with an error " +
                    "response for some reason.");
            System.out.println("Error Message:    " + ase.getMessage());
            System.out.println("HTTP Status Code: " + ase.getStatusCode());
            System.out.println("AWS Error Code:   " + ase.getErrorCode());
            System.out.println("Error Type:       " + ase.getErrorType());
            System.out.println("Request ID:       " + ase.getRequestId());
        } catch (AmazonClientException ace) {
            System.out.println("Caught an AmazonClientException, " +
                    "which means the client encountered " +
                    "an internal error while trying to " +
                    " communicate with S3, " +
                    "such as not being able to access the network.");
            System.out.println("Error Message: " + ace.getMessage());
        }
    }
}
